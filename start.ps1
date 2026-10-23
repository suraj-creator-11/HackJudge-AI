$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

if (-not (Test-Path '.venv\Scripts\python.exe')) {
    Write-Host 'Creating Python virtual environment...' -ForegroundColor Cyan
    py -3.10 -m venv .venv
}

$Python = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
Write-Host 'Installing/checking Python dependencies...' -ForegroundColor Cyan
& $Python -m pip install --upgrade pip
& $Python -m pip install -r requirements.txt

if (-not (Test-Path '.env')) {
    Copy-Item '.env.example' '.env'
    Write-Host 'Created .env. Add AI provider settings to enable semantic AI judging; baseline mode works without them.' -ForegroundColor Yellow
}

Write-Host 'Starting HackJudge AI at http://127.0.0.1:5000' -ForegroundColor Green
& $Python app.py
