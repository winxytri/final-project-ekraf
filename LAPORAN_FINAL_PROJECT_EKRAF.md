# LAPORAN FINAL PROJECT TRACK DATA ANALYTICS
## Creative Technology Future Talents Courses (Google Career Certificates x Ekraf)

---

### IDENTITAS PROYEK
- **Judul Proyek**: *Ekosistem & Akselerasi Digital UMKM Ekonomi Kreatif: Mendorong Pertumbuhan dan Pemerataan Ekonomi Daerah di Indonesia*
- **Program**: Google Career Certificates – Data Analytics Specialization x Kementerian Ekonomi Kreatif / Badan Ekonomi Kreatif (Kemenparekraf)
- **Tautan Pengumpulan**: [https://ekr.af/finalprojectda](https://ekr.af/finalprojectda)
- **Batas Pengumpulan**: 11 November 2026 (23.59 WIB)
- **Format Output**: Master Data (Excel/CSV), Dashboard Power BI (.pbix / Theme / DAX), Dashboard Interaktif (HTML), dan Infografis Resolusi Tinggi (PNG & PDF)

---

### 1. TEMA YANG DIPILIH & LATAR BELAKANG (Bobot Penilaian 15%)

#### 1.1 Relevansi Tema
Sektor Usaha Mikro, Kecil, dan Menengah (UMKM) serta Ekonomi Kreatif (Ekraf) merupakan pilar fundamental ekonomi nasional. Di Indonesia, UMKM menyumbang **97% serapan tenaga kerja nasional** dan berkontribusi terhadap **61–62% Produk Domestik Bruto (PDB)** dengan nilai potensi ekonomi mencapai lebih dari **Rp 2.194 triliun**.

Namun, di balik kontribusi besar tersebut, terdapat dua tantangan struktural mendesak:
1. **Disparitas Regional (Jawa-Sentris)**: Lebih dari 65% aktivitas ekonomi kreatif masih terpusat di Pulau Jawa, menciptakan ketimpangan produktivitas dan pendapatan antar-daerah.
2. **Kesenjangan Adopsi Digital & Akses Permodalan**: Mayoritas UMKM masih berada di tahap digitalisasi dasar (hanya menggunakan media sosial chat), dan 58% masih bergantung pada modal pribadi karena belum tersentuh perbankan formal (*unbanked/underbanked*).

Proyek ini memilih tema **"Pemanfaatan Teknologi Digital & Kontribusi UMKM Kreatif terhadap Ekonomi Daerah"**, yang membedah korelasi langsung antara adopsi teknologi digital, inklusi pembiayaan fintech produktif, dan akselerasi omzet pelaku ekonomi kreatif di 38 provinsi Indonesia.

---

### 2. KUALITAS DATA & METODOLOGI (Bobot Penilaian 20%)

#### 2.1 Kredibilitas Sumber Data
Analisis ini menggunakan dataset terpadu dari sumber resmi yang dapat dipertanggungjawabkan (*credible & reliable sources*):
1. **Kemenparekraf / Ekraf Hub (2025/2026)**:
   - Data mikro 10.478 pengguna terdaftar, mencakup status pelaku (Pemilik Usaha, Umum, Pekerja Kreatif, Asosiasi), 17 subsektor, dan sebaran geografis.
2. **Badan Pusat Statistik (BPS)**:
   - Data PDB Ekonomi Kreatif (ADHB), PDB Nasional, dan Survei Angkatan Kerja Nasional (Sakernas).
3. **Kementerian Koperasi dan UKM (KemenkopUKM)**:
   - Data agregat 65,5 juta populasi UMKM nasional, pangsa ekspor (15,7%), dan pencapaian program UMKM Go Digital.
4. **Katadata Insight Center (KIC) & Bank Indonesia**:
   - Survei Inklusi Keuangan & Pembiayaan Produktif Fintech (76,96% mitra produktif mengalami kenaikan omzet, 50.000 UMKM binaan naik kelas), serta indeks daya saing digital (*East Ventures - Digital Competitiveness Index / EV-DCI*).

#### 2.2 Proses ETL (Extract, Transform, Load)
- **Data Cleaning**: Penanganan inkonsistensi penamaan subsektor dan standardisasi 38 kode provinsi di Indonesia.
- **Data Modeling**: Pembentukan skema bintang (*Star Schema*) di Power BI yang menghubungkan tabel fakta transaksi survei pelaku (`Data_Responden_Hub`) dengan tabel dimensi subsektor (`Subsektor_Ekraf`), dimensi geografis (`Provinsi_Ekraf`), dan tren makro (`Tren_Nasional`).
- **Data Integrity**: Validasi silang antara persentase sampel Ekraf Hub dengan proporsi data sensus ekonomi BPS.

---

### 3. ANALISIS DATA, KEY INSIGHTS & STORYTELLING (Bobot Penilaian 30%)

Berdasarkan analisis statistik deskriptif dan korelasi data, dirumuskan **5 Key Insights** mendalam:

```
+----------------------------------------------------------------------------------------------------+
|                                    RINGKASAN 5 KEY INSIGHTS                                        |
+---+------------------------------------+-----------------------------------------------------------+
| # | Domain Analisis                    | Temuan Kunci Berbasis Data                                |
+---+------------------------------------+-----------------------------------------------------------+
| 1 | Dominasi Subsektor (The Big Three) | Kuliner (23.9%), Fesyen (13.6%), Kriya (9.3%) kuasai 46.8%|
|   |                                    | populasi pelaku Ekraf Hub dan >74% PDB Ekraf nasional.    |
+---+------------------------------------+-----------------------------------------------------------+
| 2 | Kesenjangan Wilayah (Jawa-Sentris) | 69.3% pelaku usaha terpusat di P. Jawa (Jabar 21.3%,      |
|   |                                    | Jatim 13.2%, DKI 11.3%, DIY 10.3%).                       |
+---+------------------------------------+-----------------------------------------------------------+
| 3 | Dampak Nyata Digitalisasi          | 80.2% UMKM "Full Digital" mengalami peningkatan omzet,   |
|   |                                    | berbanding hanya 25% pada kelompok offline.               |
+---+------------------------------------+-----------------------------------------------------------+
| 4 | Kesenjangan Akses Permodalan       | 58% UMKM masih memakai modal sendiri; penetrasi fintech   |
|   |                                    | lending baru mencapai 12% dan KUR perbankan 22%.          |
+---+------------------------------------+-----------------------------------------------------------+
| 5 | Ketahanan Tenaga Kerja             | UMKM ekraf menyerap rata-rata 3.2 naker per unit; bantalan |
|   |                                    | utama 97% penyerapan tenaga kerja nasional.               |
+---+------------------------------------+-----------------------------------------------------------+
```

#### Insight 1: Hegemoni "Big Three" dan Peluang Akselerasi Subsektor Digital
Dari 17 subsektor ekonomi kreatif, tiga subsektor konvensional mendominasi secara absolut: **Kuliner** (2.501 pelaku sampel / 23.9%), **Fesyen** (1.427 / 13.6%), dan **Kriya** (970 / 9.3%). Ketiganya menyumbang lebih dari 74% total PDB ekonomi kreatif dan 85% devisa ekspor kreatif. Namun, subsektor berbasis teknologi seperti **Aplikasi, Permainan (Game), dan Desain Komunikasi Visual (DKV)** mencatatkan laju pertumbuhan *Year-on-Year* (YoY) tertinggi (>8.5%), menandakan potensi besar ekonomi kreatif modern bernilai tambah tinggi.

#### Insight 2: Konsentrasi Geografis dan Polarisasi Jawa vs Luar Jawa
Distribusi spasial memperlihatkan konsentrasi tajam di Pulau Jawa (69.3% atau 7.257 dari 10.478 responden), dipimpin oleh Jawa Barat (2.232 pelaku), Jawa Timur (1.380), DKI Jakarta (1.183), dan DI Yogyakarta (1.083). Di luar Jawa, provinsi dengan populasi pelaku kreatif tertinggi adalah Bali (485) dan Sumatera Utara (412). Hal ini berkorelasi kuat dengan Indeks Daya Saing Digital (EV-DCI), di mana provinsi di Pulau Jawa rata-rata memiliki skor 70–85, sedangkan daerah di Indonesia Timur masih berada pada rentang 48–56.

#### Insight 3: Pembuktian Kausalitas Digitalisasi terhadap Pertumbuhan Omzet
Data membuktikan adanya korelasi positif yang sangat kuat antara kedalaman adopsi teknologi dengan stabilitas dan pertumbuhan omzet:
- Pelaku dengan status **Full Digital (Marketplace + POS Kasir Cloud)**: **80.2% mengalami kenaikan pendapatan** (42% di antaranya naik >30%, dan 38% naik antara 10–30%).
- Pelaku yang **Hanya Menggunakan Media Sosial**: 63% mengalami kenaikan pendapatan moderat.
- Pelaku **Offline / Konvensional**: 52% mengalami stagnasi pendapatan dan 23% mengalami penurunan omzet.

#### Insight 4: Paradoks Permodalan dan Peluang Financial Technology
Meskipun pembiayaan merupakan katalis utama kenaikan kelas UMKM (sebagaimana terbukti pada studi Amartha di mana 76.96% mitra pembiayaan mengalami kenaikan pendapatan), **58% pelaku ekraf masih mengandalkan modal pribadi/tabungan keluarga**. Penetrasi Kredit Usaha Rakyat (KUR) perbankan baru mencapai 22%, dan Fintech P2P Lending berizin OJK berada di angka 12%. Hambatan utama adalah ketiadaan agunan fisik dan belum tersusunnya pembukuan keuangan digital yang rapi.

#### Insight 5: Multiplier Effect Lapangan Kerja Akar Rumput
Setiap satu unit usaha mikro-kecil ekraf mampu menyerap rata-rata 2 hingga 4 tenaga kerja lokal non-formal. Di tingkat makro, hal ini menopang 25.6 juta tenaga kerja ekonomi kreatif nasional dan mengamankan mata pencaharian masyarakat di tengah gejolak otomatisasi dan perlambatan industri manufaktur padat modal.

---

### 4. VISUALISASI DATA (Bobot Penilaian 20%)

Visualisasi dirancang dengan prinsip **keterbacaan tinggi, akurasi visual, dan ramah masyarakat umum**:
1. **Donut Chart (Status Pengguna)**: Menunjukkan peran ekosistem (Pemilik Usaha 60.3%, Umum 26.4%, Pekerja Kreatif 12.6%, Asosiasi 0.6%) dengan lubang tengah 65% untuk ruang label ringkas.
2. **Horizontal Bar Chart (Top Subsektor Ekraf)**: Mengurutkan subsektor dari terbesar ke terkecil dengan kode warna berbeda (*amber orange* untuk Big 3, *cyan blue* untuk tech/media).
3. **Regional Breakdown Bar / Treemap (Sebaran Provinsi)**: Menampilkan disparitas Jawa vs Luar Jawa secara intuitif.
4. **Stacked Bar Chart (Dampak Digitalisasi)**: Menampilkan perbandingan distribusi performa pendapatan (Naik >30%, Naik 10-30%, Tetap, Menurun) berdasarkan tingkat kedewasaan digital.
5. **Kartu Skor Metrik (KPI Cards)**: Menampilkan 5 indikator utama secara tebal, jelas, dan kontras.

---

### 5. REKOMENDASI STRATEGIS & KESIMPULAN (Bobot Penilaian 15%)

Berdasarkan temuan data, dirumuskan **4 Rekomendasi Kebijakan Actionable**:

1. **Desentralisasi Infrastruktur & Insentif Logistik Luar Jawa**:
   - Pemerintah dan asosiasi e-commerce perlu memperluas program subsidi ongkos kirim dan membangun sentra logistik bersama (*shared fulfillment center*) di kota-kota strategis luar Jawa (Medan, Makassar, Balikpapan, Denpasar) untuk menurunkan *shipping barrier* produk kriya dan fesyen daerah.
2. **Inovasi Pembiayaan Alternatif Berbasis *Credit Scoring* Digital**:
   - Mendorong integrasi data transaksi Ekraf Hub dan e-commerce dengan platform Fintech P2P lending dan perbankan penyalur KUR. Rekam jejak penjualan digital dapat dijadikan pengganti agunan konvensional bagi UMKM *unbanked*.
3. **Program Akselerasi Ekspor untuk Subsektor Fesyen & Kriya**:
   - Membangun kurasi produk berstandar global, fasilitasi sertifikasi ramah lingkungan (*sustainable crafts*), dan pameran *buyer matching* internasional terkoordinasi untuk mendongkrak devisa ekraf yang saat ini baru mencapai 15.7% dari total ekspor nasional.
4. **Pendampingan "Naik Kelas" dari Medsos ke Ekosistem Full-Digital**:
   - Melakukan pelatihan intensif bagi 45% UMKM yang saat ini masih terjebak di tahap "Medsos Saja" agar mengadopsi pencatatan kasir digital (POS) dan katalog marketplace terpadu demi peningkatan omzet di atas 30%.

---

### 6. PANDUAN PENGUMPULAN (SUBMISSION CHECKLIST)

Sebelum mengunggah berkas ke portal **https://ekr.af/finalprojectda** pada tanggal **11 November 2026**, pastikan kelengkapan berkas berikut:

| No | Komponen Berkas | Lokasi File di Komputer | Status |
| :--- | :--- | :--- | :--- |
| 1 | **Infografis Final (PNG / PDF)** | `D:\final-project-ekraf\output\infografis_ekraf_final_project.png` | **Siap Unggah** |
| 2 | **Master Dataset Excel** | `D:\final-project-ekraf\data\final_project_ekraf_master_data.xlsx` | **Tersedia** |
| 3 | **Model Data & DAX Measures** | `D:\final-project-ekraf\power_bi\DAX_MEASURES.dax` | **Tersedia** |
| 4 | **Tema Power BI Resmi Ekraf** | `D:\final-project-ekraf\power_bi\Ekraf_Theme.json` | **Tersedia** |
| 5 | **Panduan Step-by-Step Power BI** | `D:\final-project-ekraf\power_bi\PANDUAN_POWER_BI.md` | **Tersedia** |
| 6 | **Dashboard Interaktif Web** | `D:\final-project-ekraf\dashboard\index.html` | **Tersedia** |
| 7 | **Metadata & Kamus Data** | `D:\final-project-ekraf\data\DATA_DICTIONARY_DAN_METODOLOGI.md` | **Tersedia** |
