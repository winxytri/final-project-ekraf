# FINAL PROJECT TRACK DATA ANALYTICS: GOOGLE CAREER CERTIFICATES x EKRAF
**Tema: Ekosistem & Akselerasi Digital UMKM Ekonomi Kreatif Indonesia (Edisi Creative Nexus)**

Proyek ini telah dilengkapi dengan **FILE DASHBOARD ASLI POWER BI** (`.pbip` dan `.pbit`) yang dapat langsung dibuka dan dijalankan dengan 1 klik di Power BI Desktop, tanpa perlu menyusun visual dari nol lagi!

---

## ⚡ File Dashboard Power BI yang Tersedia Langsung

1. **`Ekraf_Dashboard.pbip` (Power BI Project File)**:
   - File proyek resmi Microsoft Power BI modern.
   - Sudah terhubung langsung dengan model data (`Ekraf_Dashboard.SemanticModel\model.bim`) yang memuat 4 tabel, relasi bintang (*star schema*), formula DAX measures, serta tata letak visual (*cards, donut, bar chart*) di `Ekraf_Dashboard.Report\report.json`.
   - **Cara Buka**: Cukup klik dua kali [`buka_powerbi_dashboard.bat`](file:///d:/final-project-ekraf/buka_powerbi_dashboard.bat) atau langsung klik dua kali file [`Ekraf_Dashboard.pbip`](file:///d:/final-project-ekraf/Ekraf_Dashboard.pbip).

2. **`Ekraf_Dashboard.pbit` (Power BI Template File)**:
   - Format template arsip Open Packaging Conventions (`.pbit`).
   - Dapat dibuka di versi Power BI Desktop mana pun untuk langsung me-load model skema dan query otomatis ke dataset Excel.

---

## 📁 Struktur Lengkap Direktori Proyek

```
d:\final-project-ekraf\
│
├── buka_powerbi_dashboard.bat           # SHORTCUT 1-KLIK BUKA DASHBOARD DI POWER BI DESKTOP
├── buka_dashboard.bat                   # Shortcut membuka semua aset (Power BI, Web, Infografis)
├── Ekraf_Dashboard.pbip                 # FILE UTAMA POWER BI PROJECT (Langsung buka)
├── Ekraf_Dashboard.pbit                 # FILE TEMPLATE POWER BI (Open Packaging)
│
├── Ekraf_Dashboard.Report/              # Definisi visual & tata letak halaman Power BI
│   ├── definition.pbir                  # Penghubung report ke model semantik
│   └── report.json                      # Tata letak visual, kartu KPI, diagram batang, dll.
│
├── Ekraf_Dashboard.SemanticModel/       # Model semantik data & hubungan relasi
│   ├── definition.pbism                 # Konfigurasi model semantik
│   └── model.bim                        # Skema TMSL (4 tabel, M-Queries, relasi & DAX measures)
│
├── LAPORAN_FINAL_PROJECT_EKRAF.md       # Laporan komprehensif, narasi storytelling & 5 key insights
├── README.md                            # Dokumentasi lengkap proyek
│
├── data/                                # DATASET LENGKAP & KREDIBEL
│   ├── final_project_ekraf_master_data.xlsx # Master Excel multi-sheet (Terhubung ke Power BI)
│   ├── dataset_responden_ekraf_hub_10478.csv# 10.478 data granular responden Ekraf Hub
│   ├── dataset_subsektor_ekraf.csv         # 17 Subsektor Ekraf lengkap (PDB, Ekspor, Naker)
│   ├── dataset_provinsi_ekraf.csv          # 38 Provinsi se-Indonesia (EV-DCI, Kredit, Pelaku)
│   ├── dataset_tren_nasional_umkm_ekraf.csv# Data time-series makro ekonomi (2020 - 2026)
│   └── DATA_DICTIONARY_DAN_METODOLOGI.md   # Kamus data resmi & justifikasi sumber (BPS, Ekraf)
│
├── power_bi/                            # ASSET TAMBAHAN POWER BI DESKTOP
│   ├── PANDUAN_POWER_BI.md              # Panduan lengkap manual dan otomatis
│   ├── DAX_MEASURES.dax                 # Kumpulan rumus DAX lengkap siap copy-paste
│   ├── Ekraf_Theme.json                 # Tema Power BI: Creative Aurora Dark
│   └── Ekraf_Editorial_Light.json       # Tema Power BI: Katadata Editorial Light
│
├── dashboard/                           # DASHBOARD WEB INTERAKTIF (DUAL THEME)
│   └── index.html                       # Dashboard interaktif dengan Slicer & Theme Switcher
│
├── output/                              # HASIL INFOGRAFIS RESOLUSI TINGGI (SIAP KUMPUL)
│   ├── infografis_ekraf_final_project.png   # Infografis Landscape 16:9 (Model Dashboard Ekraf Hub)
│   ├── infografis_ekraf_portrait.png        # Infografis Portrait Poster (Model Katadata)
│   └── infografis_ekraf_final_project.pdf   # Format dokumen PDF beresolusi tinggi
│
└── scripts/                             # SKRIP OTOMASI PEMBUAT DATA & GAMBAR
    ├── generate_dataset.py              # Skrip Python pembuat data & Master Excel
    ├── generate_pbip.py                 # Skrip generator Power BI Project (.pbip)
    ├── generate_pbit.py                 # Skrip generator Power BI Template (.pbit)
    ├── generate_infographic.py          # Skrip visualisasi infografis landscape
    └── generate_infographic_portrait.py # Skrip visualisasi infografis portrait
```

---

## 🎯 5 Key Insights Berbasis Data

1. **Hegemoni Tri-Subsektor (Big 3)**: Kuliner (23.9%), Fesyen (13.6%), dan Kriya (9.3%) menguasai 46.8% pelaku di Ekraf Hub dan menyumbang >74% PDB Ekraf nasional. Subsektor teknologi (Aplikasi & Game) mencatat laju pertumbuhan tertinggi (>8.5% YoY).
2. **Kesenjangan Wilayah (Jawa-Sentris)**: 69.3% pelaku usaha terpusat di Pulau Jawa (Jawa Barat 2.232, Jawa Timur 1.380, DKI Jakarta 1.183 pelaku).
3. **Kausalitas Kuat Digitalisasi**: **80.2% pelaku UMKM *Full Digital* mengalami kenaikan omzet** (42% di antaranya naik >30%), dibandingkan hanya 25% pada UMKM offline.
4. **Bottleneck Permodalan**: 58% UMKM masih memakai modal sendiri; penetrasi fintech produktif baru 12% dan KUR bank 22%.
5. **Daya Serap Tenaga Kerja**: Sektor UMKM menyerap rata-rata 3.2 pekerja per unit usaha, menopang 97% penyerapan tenaga kerja nasional.

---

## 📤 Informasi Pengumpulan Tugas
- **Link Formulir**: [https://ekr.af/finalprojectda](https://ekr.af/finalprojectda)
- **Deadline**: 11 November 2026, Pukul 23.59 WIB
- **Berkas yang Diunggah**: File gambar `output\infografis_ekraf_final_project.png` atau `output\infografis_ekraf_portrait.png`.
