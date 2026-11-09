# PANDUAN STRUKTUR DASHBOARD POWER BI (DISINKRONKAN 100% DENGAN INDEX.HTML)
## Final Project Data Analytics: Google Career Certificates x Ekraf

File Power BI (`Ekraf_Dashboard.pbip` dan `Ekraf_Dashboard.pbit`) telah **disinkronkan 100% dengan tampilan 3 tab pada dashboard web (`dashboard/index.html`)**.

Ketika Anda membuka dashboard di Power BI Desktop, Anda akan menemukan **3 Halaman Utama (Tab di bagian bawah canvas)** yang persis merefleksikan 3 tab di web:

---

### 📑 Halaman 1: "1. Overview Ekosistem Ekraf" (Sesuai Tab 1)
- **Header Title**: *"EKOSISTEM & AKSELERASI DIGITAL UMKM EKONOMI KREATIF | Google Career Certificates x Kemenparekraf RI"*
- **Slicers Interaktif (Pojok Kanan Atas)**:
  - Slicer 1: `Data_Responden_Hub[Wilayah_Pulau]`
  - Slicer 2: `Data_Responden_Hub[Status_Pengguna]`
- **5 Kartu KPI Utama**:
  1. *Total Pelaku Ekraf Hub*: `10,478`
  2. *% Pemilik Usaha Mandiri*: `60.3%` (6.323 unit usaha)
  3. *% Konsentrasi Jawa*: `69.3%` (7.257 pelaku di 6 provinsi Jawa)
  4. *% Full Digital (POS + E-Com)*: `36.4%` (3.814 pelaku)
  5. *% Kenaikan Omzet Mitra*: `76.9%`
- **Visualisasi Utama**:
  - **Donut Chart**: Status Pelaku (`Data_Responden_Hub[Status_Pengguna]` vs `Total_Pengguna_Terdaftar`).
  - **Horizontal Bar Chart**: Top 12 Subsektor Ekraf (`Subsektor_Ekraf[Subsektor]`).
  - **Regional Bar Chart**: Sebaran Pelaku per Provinsi (`Provinsi_Ekraf[Provinsi]`).
- **Kotak Storytelling Bawah**: Rangkuman 5 Key Insights & Rekomendasi Aksi Kebijakan.

---

### 📑 Halaman 2: "2. Digitalisasi & Permodalan" (Sesuai Tab 2)
- **Header Title**: *"ANALISIS TRANSFORMASI DIGITAL & INKLUSI FINTECH UMKM"*
- **Slicers Interaktif**:
  - Slicer 1: `Data_Responden_Hub[Tingkat_Digitalisasi]`
  - Slicer 2: `Data_Responden_Hub[Skala_Usaha]`
- **4 Kartu Metrik Khusus**:
  1. *Pelaku Full Digital*: `3,814`
  2. *Penetrasi Fintech P2P*: `12.0%`
  3. *Rata-Rata Omzet Bulanan*: `Rp 32.5 Juta`
  4. *Total Tenaga Kerja Terserap*: `33.529 Orang` (Sampel Hub)
- **Visualisasi Utama**:
  - **100% Stacked Column Chart**: Dampak Tingkat Digital terhadap Pertumbuhan Omzet (Membandingkan *Full Digital*, *Medsos*, dan *Offline* terhadap porsi kenaikan omzet >30%, 10-30%, tetap, dan turun).
  - **Horizontal Bar Chart**: Distribusi Sumber Permodalan Pelaku Ekraf (Modal Sendiri 58%, KUR 22%, Fintech 12%, Koperasi 5%, Bantuan Pemerintah 3%).

---

### 📑 Halaman 3: "3. Eksplorasi 17 Subsektor" (Sesuai Tab 3)
- **Header Title**: *"EKSPLORASI DATA 17 SUBSEKTOR EKONOMI KREATIF INDONESIA"*
- **Slicer Interaktif**:
  - Slicer: `Subsektor_Ekraf[Kategori_Klaster]` (*Big Three*, *Tech & Media*, *Arts & Design*)
- **3 Kartu KPI Makro**:
  1. *Total PDB Ekraf Nasional*: `Rp 1.610,0 Triliun`
  2. *Total Nilai Ekspor Ekraf*: `$34,8 Miliar USD`
  3. *Rata-Rata Pertumbuhan YoY*: `6,4%`
- **Visualisasi Utama**:
  - **Tabel Data Lengkap (TableEx)**: Menampilkan 17 subsektor lengkap dengan nama klaster, pelaku sampel hub, nilai PDB, devisa ekspor, % adopsi digital, dan % pertumbuhan YoY.
  - **Bar Chart Komparasi Ekspor**: Peringkat devisa ekspor subsektor (Fesyen $18,5B, Kriya $10,8B, Kuliner $3,4B).

---

### 🚀 Cara Membuka Dashboard di Power BI Desktop
1. Cukup klik dua kali file shortcut:
   [`d:\final-project-ekraf\buka_powerbi_dashboard.bat`](file:///d:/final-project-ekraf/buka_powerbi_dashboard.bat)
2. Atau langsung klik dua kali file proyek:
   [`d:\final-project-ekraf\Ekraf_Dashboard.pbip`](file:///d:/final-project-ekraf/Ekraf_Dashboard.pbip)
3. Power BI Desktop akan terbuka dengan **3 tab halaman** di bagian bawah layar yang siap digunakan untuk presentasi!
