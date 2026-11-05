# Packs chanda and Claude's project memory into one .tar.gz for the Linux server; see docs/SERVER.md.
param([string]$Out = '')

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$pipe = Join-Path $root 'connections\pipeline'
$downloads = Join-Path $env:USERPROFILE 'Downloads'
if (-not $Out) { $Out = Join-Path $(if (Test-Path $downloads) { $downloads } else { $env:TEMP }) "chanda-$(Get-Date -Format yyyyMMdd-HHmm).tar.gz" }
$stage = Join-Path $env:TEMP "chanda-pack-$PID"
$dest = Join-Path $stage 'chanda'
$memory = Join-Path $env:USERPROFILE ('.claude\projects\' + ($root -replace '[^A-Za-z0-9]', '-') + '\memory')

$m = $null
foreach ($n in 'Global\PhysicsConnectionsPipeline', 'Local\PhysicsConnectionsPipeline') {
    if ([System.Threading.Mutex]::TryOpenExisting($n, [ref]$m)) { $m.Dispose(); throw 'a pipeline run is active on this PC; pack after it finishes' }
}
if (Get-ScheduledTask -TaskName 'PhysicsConnectionsPipeline' -ErrorAction SilentlyContinue) {
    Write-Warning 'the Windows task is still registered; its next run hands off and removes itself, but unregister it to be sure: scripts\schedule_connections.ps1 -Unregister'
}
Get-Content (Join-Path $pipe 'state.json') -Raw | ConvertFrom-Json | Out-Null

try {
    New-Item -ItemType Directory -Force $dest | Out-Null
    robocopy $root $dest /E /NFL /NDL /NJH /NJS /NP /XD __pycache__ /XF *.tmp run.lock .run.flock alerts.json settings.local.json 'state.corrupt-*.json' | Out-Null
    if ($LASTEXITCODE -ge 8) { throw "copying the project failed (robocopy exit $LASTEXITCODE)" }
    if (Test-Path $memory) {
        $memDest = New-Item -ItemType Directory -Force (Join-Path $dest '.server-memory')
        Copy-Item (Join-Path $memory '*.md') $memDest
    }
    & tar.exe -czf $Out -C $stage chanda
    if ($LASTEXITCODE -ne 0) { throw "tar failed (exit $LASTEXITCODE)" }
}
finally { Remove-Item $stage -Recurse -Force -ErrorAction SilentlyContinue }

$size = '{0:N1} MB' -f ((Get-Item $Out).Length / 1MB)
$hash = (Get-FileHash $Out -Algorithm SHA256).Hash.ToLower()
$name = Split-Path $Out -Leaf
Write-Host "packed $Out ($size)"
Write-Host "sha256 $hash"
Write-Host ''
Write-Host 'copy it to the server, e.g.:'
Write-Host "  scp `"$Out`" USER@SERVER:~/"
Write-Host 'then on the server:'
Write-Host "  echo '$hash  $name' | sha256sum -c && tar -xzf ~/$name -C ~ && bash ~/chanda/scripts/server/setup.sh"
