# DOKUMEN METADATA, KAMUS DATA & KREDIBILITAS SUMBER
## Final Project Data Analytics Track | Google Career Certificates x Ekraf

Dokumen ini mendokumentasikan metodologi kurasi data, kredibilitas sumber resmi, serta kamus data lengkap untuk proyek analisis UMKM dan Ekonomi Kreatif Indonesia.

---

### 1. Kredibilitas Sumber Data Resmi (Data Credibility & Provenance)

Dataset proyek ini dibangun dan diselaraskan secara ketat dengan publikasi data resmi otoritas nasional:

1. **Kementerian Pariwisata dan Ekonomi Kreatif / Badan Pariwisata dan Ekonomi Kreatif (Kemenparekraf/Baparekraf)**:
   - *Platform*: Ekraf Hub (Sistem Informasi dan Registrasi Pelaku Ekonomi Kreatif Nasional).
   - *Publikasi*: Statistik Ekonomi Kreatif 2023–2025 & Outlook Ekonomi Kreatif.
   - *Cakupan*: Data granular 17 subsektor ekonomi kreatif, status kepemilikan usaha, sebaran geografis di 38 provinsi Indonesia.
2. **Badan Pusat Statistik (BPS)**:
   - *Publikasi*: Produk Domestik Bruto (PDB) Atas Dasar Harga Berlaku (ADHB) menurut Lapangan Usaha dan Sektor Ekonomi Kreatif, Survei Angkatan Kerja Nasional (Sakernas), dan Sensus Ekonomi.
   - *Cakupan*: Kontribusi PDB nasional UMKM (61–62%), penyerapan tenaga kerja UMKM (97%), serta pertumbuhan ekspor kriya dan fesyen.
3. **Kementerian Koperasi dan Usaha Kecil dan Menengah (KemenkopUKM)**:
   - *Publikasi*: Data Perkembangan UMKM dan Usaha Besar di Indonesia.
   - *Cakupan*: Total populasi UMKM nasional (65.5 - 66.7 juta unit) dan target program *UMKM Go Digital* (30 juta UMKM terhubung ekosistem digital).
4. **Katadata Insight Center (KIC) & Bank Indonesia**:
   - *Publikasi*: *East Ventures - Digital Competitiveness Index (EV-DCI)* dan Laporan Survei Adopsi Keuangan Digital/Fintech pada Sektor Produktif UMKM.
   - *Cakupan*: Rasio peningkatan pendapatan pasca-digitalisasi (76.96% responden mitra produktif mengalami kenaikan omzet), tingkat inklusi fintech, dan indeks kesiapan digital regional.

---

### 2. Kamus Data (Data Dictionary)

#### A. Tabel: `Tren_Nasional` (Data Makroekonomi 2020–2026)
| Nama Kolom | Tipe Data | Keterangan & Definisi |
| :--- | :--- | :--- |
| `Tahun` | Integer | Tahun observasi (2020 hingga proyeksi 2026). |
| `Jumlah_UMKM_Juta` | Float | Jumlah unit UMKM aktif di Indonesia (dalam juta unit). |
| `PDB_Nasional_Triliun_IDR` | Float | Nilai Produk Domestik Bruto Indonesia harga berlaku (Triliun Rupiah). |
| `Kontribusi_UMKM_PDB_Triliun_IDR` | Float | Nilai kontribusi output riil UMKM ke PDB (Triliun Rupiah). |
| `Kontribusi_UMKM_PDB_Persen` | Float | Persentase kontribusi UMKM terhadap PDB nasional (~61 - 62%). |
| `PDB_Ekonomi_Kreatif_Triliun_IDR` | Float | Kontribusi nilai tambah bruto 17 subsektor ekraf ke PDB (Triliun Rupiah). |
| `Kontribusi_Ekraf_PDB_Persen` | Float | Pangsa PDB ekonomi kreatif terhadap PDB nasional (~6.8 - 7.0%). |
| `Tenaga_Kerja_UMKM_Juta` | Float | Jumlah tenaga kerja yang dipekerjakan sektor UMKM (dalam juta jiwa). |
| `Serapan_Naker_UMKM_Persen` | Float | Rasio serapan tenaga kerja UMKM terhadap total angkatan kerja nasional (97%). |
| `Tenaga_Kerja_Ekraf_Juta` | Float | Jumlah pekerja pada sektor ekonomi kreatif nasional (juta jiwa). |
| `Ekspor_Ekraf_Miliar_USD` | Float | Nilai devisa hasil ekspor komoditas ekraf (Miliar USD). |
| `UMKM_Go_Digital_Juta` | Float | Jumlah akumulatif UMKM yang telah onboarding ke platform digital. |
| `Penetrasi_Digital_Persen` | Float | Rasio UMKM digital terhadap total populasi UMKM nasional. |
| `Penyaluran_Kredit_Fintech_Triliun_IDR` | Float | Akumulasi pinjaman produktif tersalurkan oleh fintech P2P / keuangan digital berizin OJK ke sektor UMKM. |

#### B. Tabel: `Subsektor_Ekraf` (17 Subsektor Ekonomi Kreatif)
| Nama Kolom | Tipe Data | Keterangan & Definisi |
| :--- | :--- | :--- |
| `Subsektor` | Text | Nama resmi subsektor ekonomi kreatif sesuai nomenklatur Kemenparekraf. |
| `Pelaku_Sampel_Hub` | Integer | Jumlah pelaku usaha terdata pada platform Ekraf Hub (benchmark Slide 6). |
| `Estimasi_Pelaku_Nasional` | Integer | Estimasi jumlah pelaku usaha aktif se-Indonesia (skala nasional ~8.5 juta). |
| `Porsi_Pelaku_Persen` | Float | Pangsa pelaku subsektor terhadap total populasi pelaku kreatif. |
| `PDB_Ekraf_Triliun_IDR` | Float | Kontribusi nominal subsektor terhadap PDB Ekraf (Triliun Rupiah). |
| `Porsi_PDB_Persen` | Float | Pangsa subsektor terhadap total PDB Ekraf nasional. |
| `Tenaga_Kerja_Ribu_Orang` | Integer | Estimasi penyerapan tenaga kerja (dalam ribuan orang). |
| `Nilai_Ekspor_Juta_USD` | Float | Kontribusi ekspor komoditas subsektor ke pasar global (Juta USD). |
| `Tingkat_Adopsi_Digital_Persen` | Float | Persentase pelaku subsektor yang memanfaatkan perangkat lunak/platform digital. |
| `Tingkat_Inklusi_Fintech_Persen` | Float | Persentase pelaku yang mengakses fasilitas pembiayaan digital / non-bank. |
| `Pertumbuhan_Omzet_YoY_Persen` | Float | Laju pertumbuhan pendapatan tahunan rata-rata (Year-on-Year). |
| `Kategori_Klaster` | Text | Pengelompokan: `Big Three (Tradisional)`, `Digital Tech & Media`, atau `Arts & Design`. |

#### C. Tabel: `Provinsi_Ekraf` (38 Provinsi Indonesia)
| Nama Kolom | Tipe Data | Keterangan & Definisi |
| :--- | :--- | :--- |
| `Provinsi` | Text | Nama resmi provinsi di Republik Indonesia (38 provinsi). |
| `Wilayah_Pulau` | Text | Kelompok kepulauan: Jawa, Sumatera, Kalimantan, Sulawesi, Bali & Nusa Tenggara, Maluku & Papua. |
| `Pelaku_Sampel_Hub` | Integer | Jumlah profil terverifikasi di platform Ekraf Hub. |
| `Estimasi_Pelaku_Daerah` | Integer | Estimasi jumlah populasi pelaku usaha kreatif di provinsi bersangkutan. |
| `Porsi_Pelaku_Persen` | Float | Pangsa pelaku provinsi terhadap total nasional. |
| `Indeks_Daya_Saing_Digital (EV-DCI)` | Float | Skor Indeks Daya Saing Digital Daerah skala 0–100 (berdasarkan rujukan East Ventures/Katadata). |
| `Adopsi_ECommerce_Persen` | Float | Persentase UMKM di provinsi yang aktif berjualan di e-commerce/marketplace. |
| `Penyaluran_Pembiayaan_Miliar_IDR` | Float | Total volume pembiayaan modal kerja tersalurkan ke pelaku daerah (Miliar IDR). |
| `Subsektor_Unggulan` | Text | Subsektor ekonomi kreatif yang menjadi lokomotif utama di provinsi terkait. |
| `Kategori_Wilayah` | Text | Klasifikasi: `Jawa (Hub Utama)` vs `Luar Jawa (Wilayah Berkembang)`. |

#### D. Tabel: `Data_Responden_Hub` (Data Mikro 10.478 Pelaku Sesuai Slide 6)
| Nama Kolom | Tipe Data | Keterangan & Definisi |
| :--- | :--- | :--- |
| `ID_Pengguna` | Text | Kode unik registrasi pelaku di Ekraf Hub (`EKRAF-XXXXXXXX`). |
| `Status_Pengguna` | Text | Peran: `Pemilik Usaha` (6.323), `Umum` (2.767), `Pekerja Kreatif` (1.321), `Asosiasi` (67). |
| `Subsektor` | Text | Subsektor kegiatan ekonomi kreatif yang digeluti. |
| `Provinsi` | Text | Domisili legal usaha pelaku kreatif. |
| `Wilayah_Pulau` | Text | Region pulau domisili usaha. |
| `Skala_Usaha` | Text | Skala aset dan omzet berdasarkan UU Cipta Kerja: `Mikro`, `Kecil`, `Menengah`. |
| `Tingkat_Digitalisasi` | Text | Derajat implementasi teknologi: `Full Digital (Marketplace & POS)`, `Media Sosial Saja`, atau `Offline / Belum Digital`. |
| `Menggunakan_Fintech_Digital` | Text | Indikator penggunaan layanan pinjaman produktif/fintech P2P lending (`Ya` / `Tidak`). |
| `Sumber_Permodalan_Utama` | Text | Modal Sendiri, Pinjaman Bank (KUR), Fintech P2P, Koperasi, Bantuan Pemerintah. |
| `Dampak_Digital_Thdp_Omzet` | Text | Persepsi kenaikan omzet: `Meningkat >30%`, `Meningkat 10-30%`, `Relatif Tetap (0-9%)`, `Mengalami Penurunan`. |
| `Omzet_Bulanan_Juta_IDR` | Float | Rata-rata pendapatan bruto bulanan (Juta Rupiah). |
| `Jumlah_Tenaga_Kerja` | Integer | Jumlah orang yang bekerja pada unit usaha tersebut. |
