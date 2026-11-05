# Register, remove or health-check the Windows scheduled task that runs run_connections.ps1 every few hours.
param([switch]$Register, [switch]$Unregister, [double]$Hours = 0, [string]$ResumeAt = '')

$ErrorActionPreference = 'Stop'
$name = 'PhysicsConnectionsPipeline'
$resumeName = "$name-Resume"
$root = Split-Path -Parent $PSScriptRoot
$runner = Join-Path $PSScriptRoot 'run_connections.ps1'
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$runner`"" -WorkingDirectory $root
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Hours 4) -MultipleInstances IgnoreNew

if ($Unregister) {
    foreach ($n in $name, $resumeName) { Unregister-ScheduledTask -TaskName $n -Confirm:$false -ErrorAction SilentlyContinue }
    Write-Output "Removed scheduled tasks $name and $resumeName (if they existed)."
    exit 0
}

if ($ResumeAt) {
    $at = [datetime]::Parse($ResumeAt)
    $trigger = New-ScheduledTaskTrigger -Once -At $at
    $trigger.EndBoundary = $at.AddHours(2).ToString('s')
    $settings.DeleteExpiredTaskAfter = 'PT1H'
    Register-ScheduledTask -TaskName $resumeName -Action $action -Trigger $trigger -Settings $settings -Force `
        -Description 'One-off resume of the physics connection pipeline just after a usage-limit reset; deletes itself.' | Out-Null
    Write-Output "Resume run scheduled for $at."
    exit 0
}

if ($Register) {
    $cfg = Get-Content (Join-Path $root 'connections\pipeline\config.json') -Raw | ConvertFrom-Json
    if ($Hours -le 0) { $Hours = [double]$cfg.interval_hours }
    $trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(3) -RepetitionInterval (New-TimeSpan -Minutes ([int]($Hours * 60))) -RepetitionDuration (New-TimeSpan -Days 365)
    Register-ScheduledTask -TaskName $name -Action $action -Trigger $trigger -Settings $settings -Force `
        -Description 'Resumes the physics connection-discovery pipeline in small headless Claude runs; removes itself when done.' | Out-Null
    Write-Output "Registered ${name}: every $Hours h for up to a year, first run in ~3 minutes."
}

function Check([string]$level, [string]$msg) { Write-Output ('{0,-4}  {1}' -f $level, $msg) }

$task = Get-ScheduledTask -TaskName $name -ErrorAction SilentlyContinue
if (-not $task) { Check 'FAIL' "scheduled task $name is not registered: run this script with -Register" }
else {
    $info = $task | Get-ScheduledTaskInfo
    Check $(if ($task.State -eq 'Disabled') { 'FAIL' } else { 'OK' }) "task $name is $($task.State): next run $($info.NextRunTime), last run $($info.LastRunTime) (result $($info.LastTaskResult))"
    if ($info.LastTaskResult -notin 0, 267009, 267011) { Check 'WARN' "the last scheduled run ended with code $($info.LastTaskResult); see connections/pipeline/runs.log" }
    $tr = @($task.Triggers)[0]
    if ($tr.Repetition.Duration) {
        $end = ([datetime]$tr.StartBoundary) + [System.Xml.XmlConvert]::ToTimeSpan($tr.Repetition.Duration)
        $days = ($end - (Get-Date)).TotalDays
        Check $(if ($days -lt 7) { 'WARN' } else { 'OK' }) ("task repeats until {0:yyyy-MM-dd} ({1:N0} days left){2}" -f $end, $days, $(if ($days -lt 7) { '; run with -Register to extend' }))
    }
    if (-not $task.Settings.StartWhenAvailable) { Check 'WARN' 'missed runs are not caught up (StartWhenAvailable is off): re-run with -Register' }
}
$resume = Get-ScheduledTask -TaskName $resumeName -ErrorAction SilentlyContinue
if ($resume) { Check 'OK' "one-off resume run pending at $(@($resume.Triggers)[0].StartBoundary)" }

$token = [Environment]::GetEnvironmentVariable('CLAUDE_CODE_OAUTH_TOKEN', 'User')
Check $(if ($token) { 'OK' } else { 'WARN' }) $(if ($token) { 'CLAUDE_CODE_OAUTH_TOKEN is set for unattended sign-in' } else { "CLAUDE_CODE_OAUTH_TOKEN is not set: unattended runs depend on the interactive login, which expires (run 'claude setup-token')" })
foreach ($exe in 'claude', 'python') {
    $all = @(Get-Command $exe -All -CommandType Application -ErrorAction SilentlyContinue)
    $cmd = @($all | Where-Object { $_.Source -notlike '*\WindowsApps\*' }) + $all | Select-Object -First 1
    Check $(if ($cmd) { 'OK' } else { 'FAIL' }) $(if ($cmd) { "$exe found at $($cmd.Source)" } else { "$exe is not on PATH for the scheduled task" })
}

$held = $false
foreach ($n in 'Global\PhysicsConnectionsPipeline', 'Local\PhysicsConnectionsPipeline') {
    $m = $null
    if ([System.Threading.Mutex]::TryOpenExisting($n, [ref]$m)) { $held = $true; $m.Dispose() }
}
$lockFile = Join-Path $root 'connections\pipeline\run.lock'
if ($held) { Check 'OK' ("a run is active now: " + [string](Get-Content $lockFile -Raw -ErrorAction SilentlyContinue)).Trim() }
elseif (Test-Path $lockFile) { Check 'OK' 'no run is active (run.lock is left over from a run that died; harmless, the next run clears it)' }
else { Check 'OK' 'no run is active' }

& python -I (Join-Path $root 'scripts\connections_pipeline.py') doctor
