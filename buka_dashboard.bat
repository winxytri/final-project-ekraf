@echo off
title Ekraf Future Talents - Dashboard Launcher
color 0A
echo ==============================================================================
echo   FINAL PROJECT DATA ANALYTICS: GOOGLE CAREER CERTIFICATES x EKRAF
echo   Tema: Ekosistem & Akselerasi Digital UMKM Ekonomi Kreatif Indonesia
echo ==============================================================================
echo.
echo Membuka seluruh berkas dashboard Anda:
echo.
echo [1] Meluncurkan Dashboard Power BI (.pbip / .pbit)...
start "" "%~dp0buka_powerbi_dashboard.bat"

echo.
echo [2] Membuka Dashboard Web Interaktif (Dual Theme: Dark/Light)...
start "" "%~dp0dashboard\index.html"

echo.
echo [3] Membuka Gambar Infografis Resolusi Tinggi (Siap Submit)...
start "" "%~dp0output\infografis_ekraf_final_project.png"

echo.
echo Selesai! Seluruh berkas siap dipresentasikan atau diunggah ke:
echo https://ekr.af/finalprojectda (Batas waktu: 11 November 2026, 23.59 WIB)
pause
