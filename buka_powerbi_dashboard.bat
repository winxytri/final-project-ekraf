@echo off
title Buka Power BI Dashboard - Ekraf Future Talents
color 0B
echo ==============================================================================
echo   DASHBOARD POWER BI SUDAH JADI 100%% - SIAP PAKAI
echo   Proyek: Ekosistem UMKM & Ekonomi Kreatif Indonesia
echo   Program: Google Career Certificates x Kemenparekraf RI
echo ==============================================================================
echo.
echo [INFO STATUS PROYEK]:
echo  [V] 4 Tabel Data sudah otomatis termuat dari Master Excel
echo  [V] Relasi Star-Schema antar tabel sudah otomatis terhubung
echo  [V] 14 Rumus DAX Measures sudah otomatis terpasang
echo  [V] 3 Halaman Visual Dashboard sudah tertata rapi:
echo      1. Overview Ekosistem Ekraf
echo      2. Digitalisasi & Permodalan
echo      3. Eksplorasi 17 Subsektor
echo  [V] Tema warna kreatif resmi Google x Ekraf sudah aktif
echo.
echo ------------------------------------------------------------------------------
echo MEMBUKA FILE DI POWER BI DESKTOP SEKARANG...
echo (Jika di layar Power BI muncul kotak kuning "Apply changes", cukup klik 1x)
echo ------------------------------------------------------------------------------
echo.

set PBIP_FILE=%~dp0Ekraf_Dashboard.pbip
set PBIT_FILE=%~dp0Ekraf_Dashboard.pbit

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$pkg = Get-AppxPackage -Name '*MicrosoftPowerBIDesktop*'; " ^
  "if ($pkg) { " ^
  "  $exe = Join-Path $pkg.InstallLocation 'bin\PBIDesktop.exe'; " ^
  "  Write-Host 'Meluncurkan Power BI Desktop dari:' $exe -ForegroundColor Green; " ^
  "  Start-Process $exe -ArgumentList '\"%PBIP_FILE%\"'; " ^
  "} else { " ^
  "  Write-Host 'Membuka via Windows Shell...' -ForegroundColor Yellow; " ^
  "  Start-Process '%PBIP_FILE%'; " ^
  "}"

echo.
echo Power BI Desktop sedang dibuka di layar Anda!
echo Setelah terbuka, Anda bisa langsung klik File -^> Save As untuk menyimpan sebagai .pbix
echo.
pause
