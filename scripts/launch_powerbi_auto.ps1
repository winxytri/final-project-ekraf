# Automation script to load template and generate pbix if user runs it
param(
    [string]$ProjectRoot = "D:\final-project-ekraf"
)

$pbipPath = Join-Path $ProjectRoot "Ekraf_Dashboard.pbip"
$pkg = Get-AppxPackage -Name "*MicrosoftPowerBIDesktop*"

if (-not $pkg) {
    Write-Host "Power BI Desktop tidak ditemukan di Windows Apps." -ForegroundColor Red
    exit
}

$exe = Join-Path $pkg.InstallLocation "bin\PBIDesktop.exe"
Write-Host "Membuka Power BI Desktop..." -ForegroundColor Cyan
$proc = Start-Process -FilePath $exe -ArgumentList "`"$pbipPath`"" -PassThru

Write-Host "Power BI Desktop telah dijalankan (PID: $($proc.Id))." -ForegroundColor Green
Write-Host "Seluruh struktur 3 halaman, tabel, dan visual sedang dimuat otomatis!" -ForegroundColor Yellow
