# One budgeted run of the connection pipeline: a few units, each a fresh headless Claude session; stops at a usage limit.
param([int]$Units = 0, [switch]$DryRun)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root
$pipe = Join-Path $root 'connections\pipeline'
$log = Join-Path $pipe 'runs.log'
$lockInfo = Join-Path $pipe 'run.lock'
$alertsFile = Join-Path $pipe 'alerts.json'
$pipeline = Join-Path $root 'scripts\connections_pipeline.py'
$scheduler = Join-Path $PSScriptRoot 'schedule_connections.ps1'
$taskName = 'PhysicsConnectionsPipeline'
$utf8 = New-Object System.Text.UTF8Encoding $false
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$env:PYTHONIOENCODING = 'utf-8'

function Log([string]$msg) {
    $line = '{0:yyyy-MM-dd HH:mm:ss}  {1}' -f (Get-Date), $msg
    [System.IO.File]::AppendAllText($log, $line + "`n", $utf8)
    Write-Host $line
}

function Find-Exe([string]$name, [string[]]$fallbacks) {
    $all = @(Get-Command $name -All -CommandType Application -ErrorAction SilentlyContinue)
    $cmd = @($all | Where-Object { $_.Source -notlike '*\WindowsApps\*' }) + $all | Select-Object -First 1
    if ($cmd) { return $cmd.Source }
    foreach ($f in $fallbacks) { if (Test-Path $f) { return $f } }
    throw "cannot find $name"
}

function Quote-Arg([string]$a) {
    if ($a -and $a -notmatch '[\s"]') { return $a }
    '"' + (($a -replace '(\\*)"', '$1$1\"') -replace '(\\+)$', '$1$1') + '"'
}

# Runs exe with argv and UTF-8 stdin, kills its whole process tree after $minutes; returns Out, Err, Code, TimedOut.
function Invoke-Bounded([string]$exe, [string[]]$argv, [double]$minutes, [string]$stdin) {
    $psi = New-Object System.Diagnostics.ProcessStartInfo $exe
    $psi.Arguments = ($argv | ForEach-Object { Quote-Arg $_ }) -join ' '
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true
    $psi.RedirectStandardInput = $true
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.StandardOutputEncoding = [System.Text.Encoding]::UTF8
    $psi.StandardErrorEncoding = [System.Text.Encoding]::UTF8
    $p = [System.Diagnostics.Process]::Start($psi)
    $out = $p.StandardOutput.ReadToEndAsync()
    $err = $p.StandardError.ReadToEndAsync()
    try {
        $bytes = $utf8.GetBytes($stdin)
        $p.StandardInput.BaseStream.Write($bytes, 0, $bytes.Length)
        $p.StandardInput.Close()
    } catch { }  # the child exited before reading stdin; its output says why
    $timedOut = -not $p.WaitForExit([int]($minutes * 60000))
    if ($timedOut) { cmd /c "taskkill /T /F /PID $($p.Id) >nul 2>&1" }
    $p.WaitForExit()
    $o = if ($out.Wait(10000)) { $out.Result } else { '' }
    $e = if ($err.Wait(10000)) { $err.Result } else { '' }
    @{ Out = $o; Err = $e; Code = $(if ($timedOut) { -1 } else { $p.ExitCode }); TimedOut = $timedOut }
}

# Runs a pipeline subcommand; logs its warnings, throws on a non-zero exit, returns its non-empty stdout lines.
function Py([string[]]$argv, [double]$minutes = 10) {
    $r = Invoke-Bounded $python (@('-I', $pipeline) + $argv) $minutes ''
    foreach ($w in @($r.Err -split "`r?`n" | Where-Object { $_ -like 'warning: *' })) { Log "pipeline $w" }
    if ($r.Code -ne 0) {
        $tail = @($r.Err.Trim() -split "`r?`n" | Where-Object { $_.Trim() }) | Select-Object -Last 1
        throw "pipeline '$($argv[0])' failed (exit $($r.Code)): $tail"
    }
    @($r.Out -split "`r?`n" | Where-Object { $_.Trim() })
}

# Desktop toast, at most once per alert key per day.
function Notify([string]$key, [string]$title, [string]$text) {
    $today = (Get-Date).ToString('yyyy-MM-dd')
    $sent = @{}
    if (Test-Path $alertsFile) {
        try { (Get-Content $alertsFile -Raw | ConvertFrom-Json).PSObject.Properties | ForEach-Object { $sent[$_.Name] = $_.Value } } catch { }
    }
    if ($sent[$key] -eq $today) { return }
    $sent[$key] = $today
    try { [System.IO.File]::WriteAllText($alertsFile, ($sent | ConvertTo-Json), $utf8) } catch { }
    Log "ALERT ${title}: $text"
    try {
        [void][Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]
        [void][Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime]
        $xml = New-Object Windows.Data.Xml.Dom.XmlDocument
        $esc = { param($s) [Security.SecurityElement]::Escape($s) }
        $xml.LoadXml("<toast><visual><binding template='ToastGeneric'><text>$(& $esc $title)</text><text>$(& $esc $text)</text></binding></visual></toast>")
        $app = '{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe'
        [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier($app).Show([Windows.UI.Notifications.ToastNotification]::new($xml))
    } catch { Log "could not show a desktop notification: $($_.Exception.Message)" }
}

function Get-RunMutex {
    foreach ($n in 'Global\PhysicsConnectionsPipeline', 'Local\PhysicsConnectionsPipeline') {
        try { return New-Object System.Threading.Mutex($false, $n) } catch { }
    }
    throw 'cannot create the run mutex'
}

# Kills headless unit sessions whose runner died; only called while holding the mutex, before this run starts any.
function Stop-Orphans {
    $sig = '--no-session-persistence', '--strict-mcp-config', 'dontAsk'
    foreach ($p in @(Get-CimInstance Win32_Process -Filter "Name='claude.exe' OR Name='node.exe'" -ErrorAction SilentlyContinue)) {
        $cl = [string]$p.CommandLine
        if (@($sig | Where-Object { $cl -notlike "*$_*" }).Count) { continue }
        $parent = Get-CimInstance Win32_Process -Filter "ProcessId=$($p.ParentProcessId)" -ErrorAction SilentlyContinue
        if ($parent -and $parent.CreationDate -le $p.CreationDate -and [string]$parent.CommandLine -like '*run_connections*') { continue }
        cmd /c "taskkill /T /F /PID $($p.ProcessId) >nul 2>&1"
        Log "killed an orphaned unit session left by a dead run (pid $($p.ProcessId), started $($p.CreationDate))"
    }
}

$mutex = $null
$owned = $false
try {
    if ((Test-Path $log) -and (Get-Item $log).Length -gt 2MB) { Move-Item $log "$log.1" -Force }
    $python = Find-Exe 'python' @("$env:LOCALAPPDATA\Python\bin\python.exe", "$env:LOCALAPPDATA\Programs\Python\Python310\python.exe")
    $claude = Find-Exe 'claude' @("$env:USERPROFILE\.local\bin\claude.exe", "$env:APPDATA\npm\claude.cmd")
    $mutex = Get-RunMutex
    try { $owned = $mutex.WaitOne(0) }
    catch {
        if (-not ($_.Exception -is [System.Threading.AbandonedMutexException] -or $_.Exception.InnerException -is [System.Threading.AbandonedMutexException])) { throw }
        $owned = $true
        Log 'the previous run died while holding the lock; taking over'
    }
    if (-not $owned) { Log 'another run is active; exiting'; return }
    [System.IO.File]::WriteAllText($lockInfo, "pid $PID since $(Get-Date -Format s)$(if ($DryRun) { ' (dry run)' })", $utf8)
    if (-not $DryRun) {
        Stop-Orphans
        Py @('recover') | ForEach-Object { Log $_ }
    }

    $nextArgs = @('next', '-n', [string]$Units)
    if ($DryRun) { $nextArgs += '--ignore-wait' }
    $todo = @()
    $changed = $false
    foreach ($line in (Py $nextArgs 30)) {
        $f = $line -split "`t"
        if ($f[0] -eq 'UNIT') { $todo += , $f }
        elseif ($f[0] -eq 'INFO') { Log $f[1]; $changed = $true }
        elseif ($f[0] -eq 'WAIT') { Log "waiting: $($f[1])" }
        elseif ($f[0] -eq 'CAPPED') { Log 'daily unit cap reached; resuming tomorrow' }
        elseif ($f[0] -eq 'BLOCKED') { Log "blocked: $($f[1])" }
        elseif ($f[0] -eq 'HANDOFF') {
            Log "handoff: $($f[1]); removing this machine's scheduled task"
            Notify 'handoff' 'Physics pipeline handed off' $f[1]
            if (-not $DryRun) { & powershell -NoProfile -ExecutionPolicy Bypass -File $scheduler -Unregister | Out-Null }
            return
        }
        elseif ($f[0] -eq 'DONE') {
            Log 'pipeline finished; removing the scheduled task'
            Notify 'done' 'Physics connections pipeline finished' 'The registry is final: open connections/map.html.'
            if (-not $DryRun) { & powershell -NoProfile -ExecutionPolicy Bypass -File $scheduler -Unregister | Out-Null }
            return
        }
        else { Log "unexpected planner output: $line" }
    }

    $lean = @('--strict-mcp-config', '--disable-slash-commands', '--setting-sources', 'project', '--tools', 'Read,Grep,Glob')
    foreach ($f in $todo) {
        $unit, $model, $effort, $budget = $f[1], $f[2], $f[3], $f[4]
        $timeout = [double]$f[5]
        $promptFile = Join-Path $pipe "work\$unit.prompt.md"
        try { Py @('prompt', $unit, '--out', $promptFile) | Out-Null }
        catch {
            Log "${unit}: could not build its prompt ($($_.Exception.Message)); counting a failed attempt"
            if (-not $DryRun) { Py @('mark', $unit, 'running') | Out-Null; Py @('mark', $unit, 'failed', '--note', 'prompt build failed') | Out-Null }
            continue
        }
        $prompt = [System.IO.File]::ReadAllText($promptFile, [System.Text.Encoding]::UTF8)
        if ($DryRun) { Log "DRY $unit model=$model effort=$effort budget=`$$budget timeout=${timeout}min :: $($prompt.Length) chars in $promptFile"; continue }
        Py @('mark', $unit, 'running') | Out-Null
        $cargs = @('-p', '--permission-mode', 'dontAsk', '--no-session-persistence', '--output-format', 'json') + $lean
        if ($model) { $cargs += @('--model', $model) }
        if ($effort) { $cargs += @('--effort', $effort) }
        if ($budget) { $cargs += @('--max-budget-usd', $budget) }
        $cargs += @('--allowedTools', 'Read', 'Grep', 'Glob')
        $outFile = Join-Path $pipe "work\$unit.out.txt"
        $errFile = Join-Path $pipe "work\$unit.err.txt"
        Log "start $unit$(if ($model) { " on $model" })$(if ($effort) { " at $effort effort" })"
        $res = Invoke-Bounded $claude $cargs $timeout $prompt
        [System.IO.File]::WriteAllText($outFile, $res.Out, $utf8)
        [System.IO.File]::WriteAllText($errFile, $res.Err, $utf8)
        if ($res.TimedOut) { Log "$unit ran past $timeout min; killed" }
        $ingestArgs = @('ingest', $unit, $outFile, '--err', $errFile)
        if ($res.TimedOut) { $ingestArgs += '--timed-out' }
        $v = (@(Py $ingestArgs) | Select-Object -Last 1) -split "`t"
        Log "$($v[1]) (exit $($res.Code))"
        $changed = $changed -or $v[0] -eq 'OK'
        if ($v[0] -eq 'LIMIT') {
            Log "stopped by a usage limit; cooling down until $($v[2])"
            try {
                $until = [datetime]::Parse($v[2])
                $nextRun = (Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue | Get-ScheduledTaskInfo).NextRunTime
                if ($nextRun -and $until -lt $nextRun.AddMinutes(-10)) {
                    & powershell -NoProfile -ExecutionPolicy Bypass -File $scheduler -ResumeAt $v[2] | Out-Null
                    Log "scheduled a one-off resume run at $until, right after the limit resets"
                }
            } catch { Log "could not schedule a resume run: $($_.Exception.Message)" }
            break
        }
        if ($v[0] -eq 'AUTH') {
            Notify 'auth' 'Physics pipeline: Claude sign-in expired' "Run 'claude setup-token' and store the token in the user variable CLAUDE_CODE_OAUTH_TOKEN; the next run resumes."
            break
        }
        if ($v[0] -eq 'TRANSIENT') { Log "transient API trouble; the pipeline waits until $($v[2])"; break }
    }

    if (-not $DryRun) {
        if ($changed) {
            try { Py @('snapshot') 20 | ForEach-Object { Log $_ } }
            catch { Log "snapshot failed: $($_.Exception.Message)"; Notify 'snapshot' 'Physics pipeline: snapshot failed' $_.Exception.Message }
        }
        foreach ($a in @(Py @('doctor', '--alerts'))) {
            $x = $a -split "`t"
            if ($x[0] -eq 'ALERT') { Notify $x[1] 'Physics connections pipeline needs attention' $x[2] }
        }
    }
}
catch {
    $msg = "runner error: $($_.Exception.Message) (line $($_.InvocationInfo.ScriptLineNumber))"
    try { Log $msg } catch { }
    try { Notify 'runner-error' 'Physics connections pipeline failed' $msg } catch { }
    exit 1
}
finally {
    if ($owned) {
        Remove-Item $lockInfo -ErrorAction SilentlyContinue
        try { $mutex.ReleaseMutex() } catch { }
    }
    if ($mutex) { $mutex.Dispose() }
}
