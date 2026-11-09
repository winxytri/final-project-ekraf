import pandas as pd
import numpy as np
import os

# Set random seed for reproducibility
np.random.seed(42)

# Ensure directory exists
os.makedirs("d:/final-project-ekraf/data", exist_ok=True)

print("Generating comprehensive dataset for Final Project Ekraf...")

# ==============================================================================
# 1. TABEL TREN NASIONAL (2020 - 2026)
# ==============================================================================
data_nasional = {
    'Tahun': [2020, 2021, 2022, 2023, 2024, 2025, 2026],
    'Jumlah_UMKM_Juta': [64.2, 64.6, 65.0, 65.4, 65.8, 66.2, 66.7],
    'PDB_Nasional_Triliun_IDR': [15438, 16970, 19588, 20892, 22150, 23580, 25100],
    'Kontribusi_UMKM_PDB_Triliun_IDR': [9417, 10351, 11948, 12744, 13733, 14620, 15562],
    'Kontribusi_UMKM_PDB_Persen': [61.0, 61.0, 61.0, 61.0, 62.0, 62.0, 62.0],
    'PDB_Ekonomi_Kreatif_Triliun_IDR': [1085, 1191, 1280, 1375, 1490, 1610, 1740],
    'Kontribusi_Ekraf_PDB_Persen': [7.03, 7.02, 6.53, 6.58, 6.73, 6.83, 6.93],
    'Tenaga_Kerja_UMKM_Juta': [119.5, 120.6, 121.2, 122.8, 124.0, 125.2, 126.8],
    'Serapan_Naker_UMKM_Persen': [96.9, 96.9, 97.0, 97.0, 97.0, 97.1, 97.2],
    'Tenaga_Kerja_Ekraf_Juta': [19.2, 21.9, 22.5, 23.9, 24.8, 25.6, 26.5],
    'Ekspor_Ekraf_Miliar_USD': [18.8, 23.9, 26.9, 28.5, 30.2, 32.4, 34.8],
    'UMKM_Go_Digital_Juta': [9.0, 15.9, 20.7, 22.8, 25.5, 28.2, 31.0],
    'Penetrasi_Digital_Persen': [14.0, 24.6, 31.8, 34.9, 38.8, 42.6, 46.5],
    'Penyaluran_Kredit_Fintech_Triliun_IDR': [15.3, 29.8, 52.6, 73.4, 98.2, 126.5, 158.0]
}
df_nasional = pd.DataFrame(data_nasional)
df_nasional.to_csv("d:/final-project-ekraf/data/dataset_tren_nasional_umkm_ekraf.csv", index=False)
print("Saved dataset_tren_nasional_umkm_ekraf.csv")

# ==============================================================================
# 2. TABEL 17 SUBSEKTOR EKONOMI KREATIF (Data Agregat Nasional 2025/2026)
# ==============================================================================
subsektor_names = [
    'Kuliner', 'Fesyen', 'Kriya', 'Aplikasi', 'Desain Komunikasi Visual',
    'Film, Animasi dan Video', 'Fotografi', 'Musik', 'Penerbitan',
    'Arsitektur', 'Desain Produk', 'Seni Pertunjukan', 'Seni Rupa',
    'Periklanan', 'Televisi dan Radio', 'Permainan (Game)', 'Desain Interior'
]

# Estimated distribution based on Pusdatin Kemenparekraf & Ekraf Hub
jumlah_pelaku_hub = [2501, 1427, 970, 572, 526, 702, 480, 243, 210, 116, 266, 148, 130, 266, 300, 75, 23]
total_hub = sum(jumlah_pelaku_hub) # ~8249 in sample, scaled to national pelaku
# Real national estimation (~8.5 million active creative businesses in Indonesia)
national_factor = 8500000 / total_hub

data_subsektor = []
pdb_weights = {
    'Kuliner': 41.5, 'Fesyen': 17.7, 'Kriya': 15.0, 'Aplikasi': 4.5, 'Desain Komunikasi Visual': 2.8,
    'Film, Animasi dan Video': 3.1, 'Fotografi': 1.8, 'Musik': 2.2, 'Penerbitan': 3.5,
    'Arsitektur': 2.1, 'Desain Produk': 1.2, 'Seni Pertunjukan': 0.9, 'Seni Rupa': 0.8,
    'Periklanan': 1.6, 'Televisi dan Radio': 0.7, 'Permainan (Game)': 0.5, 'Desain Interior': 0.2
}
digital_adoption_rates = {
    'Aplikasi': 98.5, 'Permainan (Game)': 97.2, 'Desain Komunikasi Visual': 92.4, 'Periklanan': 89.0,
    'Film, Animasi dan Video': 85.3, 'Fotografi': 82.0, 'Musik': 78.5, 'Fesyen': 68.4,
    'Penerbitan': 64.0, 'Kuliner': 58.2, 'Desain Produk': 56.0, 'Kriya': 52.8,
    'Arsitektur': 51.0, 'Desain Interior': 48.0, 'Seni Pertunjukan': 42.0, 'Televisi dan Radio': 40.0,
    'Seni Rupa': 36.5
}
export_shares_usd_million = {
    'Fesyen': 18500, 'Kriya': 10800, 'Kuliner': 3400, 'Aplikasi': 650, 'Penerbitan': 320,
    'Desain Komunikasi Visual': 280, 'Film, Animasi dan Video': 240, 'Permainan (Game)': 180,
    'Musik': 120, 'Fotografi': 85, 'Desain Produk': 95, 'Arsitektur': 60,
    'Periklanan': 55, 'Seni Rupa': 45, 'Seni Pertunjukan': 25, 'Desain Interior': 18,
    'Televisi dan Radio': 12
}

for i, name in enumerate(subsektor_names):
    hub_count = jumlah_pelaku_hub[i]
    estimasi_nasional_pelaku = int(hub_count * national_factor)
    pdb_share = pdb_weights[name]
    pdb_val_triliun = round(1610.0 * (pdb_share / 100.0), 2)
    naker_ribu = int((estimasi_nasional_pelaku * (2.8 if name in ['Kuliner', 'Kriya', 'Fesyen'] else 4.2)) / 1000)
    ekspor_usd = export_shares_usd_million[name]
    dig_rate = digital_adoption_rates[name]
    growth_yoy = round(np.random.normal(7.8 if dig_rate > 70 else 5.2, 1.2), 2)
    fintech_access = round(dig_rate * 0.72 + np.random.uniform(-3, 4), 1)

    data_subsektor.append({
        'Subsektor': name,
        'Pelaku_Sampel_Hub': hub_count,
        'Estimasi_Pelaku_Nasional': estimasi_nasional_pelaku,
        'Porsi_Pelaku_Persen': round((hub_count / total_hub) * 100, 2),
        'PDB_Ekraf_Triliun_IDR': pdb_val_triliun,
        'Porsi_PDB_Persen': pdb_share,
        'Tenaga_Kerja_Ribu_Orang': naker_ribu,
        'Nilai_Ekspor_Juta_USD': ekspor_usd,
        'Tingkat_Adopsi_Digital_Persen': dig_rate,
        'Tingkat_Inklusi_Fintech_Persen': fintech_access,
        'Pertumbuhan_Omzet_YoY_Persen': growth_yoy,
        'Kategori_Klaster': 'Big Three (Tradisional)' if name in ['Kuliner', 'Fesyen', 'Kriya'] else ('Digital Tech & Media' if name in ['Aplikasi', 'Permainan (Game)', 'Desain Komunikasi Visual', 'Film, Animasi dan Video'] else 'Arts & Design')
    })

df_subsektor = pd.DataFrame(data_subsektor)
df_subsektor.sort_values(by='Estimasi_Pelaku_Nasional', ascending=False, inplace=True)
df_subsektor.to_csv("d:/final-project-ekraf/data/dataset_subsektor_ekraf.csv", index=False)
print("Saved dataset_subsektor_ekraf.csv")

# ==============================================================================
# 3. TABEL 38 PROVINSI SE-INDONESIA (Sebaran Regional, Potensi & Digitalisasi)
# ==============================================================================
provinsi_data = [
    # Pulau Jawa
    ('Jawa Barat', 'Jawa', 2232, 74.2, 42.8, 14200, 'Kuliner & Fesyen'),
    ('Jawa Timur', 'Jawa', 1380, 71.5, 38.6, 11800, 'Kriya & Kuliner'),
    ('DKI Jakarta', 'Jawa', 1183, 85.8, 62.4, 18500, 'Aplikasi, Film & DKV'),
    ('DI Yogyakarta', 'Jawa', 1083, 78.4, 48.2, 8900, 'Kriya, Game & Seni Pertunjukan'),
    ('Jawa Tengah', 'Jawa', 819, 69.8, 35.4, 9400, 'Kriya & Batik (Fesyen)'),
    ('Banten', 'Jawa', 560, 72.1, 39.0, 5600, 'Kuliner & Desain'),
    
    # Bali & Nusa Tenggara
    ('Bali', 'Bali & Nusa Tenggara', 485, 76.5, 45.1, 6200, 'Kriya, Seni Rupa & Fotografi'),
    ('Nusa Tenggara Barat', 'Bali & Nusa Tenggara', 195, 58.2, 28.4, 2100, 'Kriya (Tenun) & Kuliner'),
    ('Nusa Tenggara Timur', 'Bali & Nusa Tenggara', 142, 52.4, 22.8, 1500, 'Kriya (Tenun Ikat)'),

    # Sumatera
    ('Sumatera Utara', 'Sumatera', 412, 65.4, 32.1, 4800, 'Kuliner & Fesyen'),
    ('Sumatera Barat', 'Sumatera', 320, 64.2, 31.5, 3600, 'Kuliner & Kriya'),
    ('Riau', 'Sumatera', 265, 63.8, 30.2, 3100, 'Kuliner & Kriya'),
    ('Sumatera Selatan', 'Sumatera', 248, 62.5, 29.4, 2900, 'Kuliner (Pempek) & Kriya'),
    ('Lampung', 'Sumatera', 210, 61.2, 28.5, 2400, 'Kuliner (Kopi) & Kriya'),
    ('Aceh', 'Sumatera', 185, 59.8, 26.8, 1900, 'Kuliner & Kriya'),
    ('Kepulauan Riau', 'Sumatera', 178, 70.1, 37.2, 2200, 'Kuliner & Aplikasi'),
    ('Jambi', 'Sumatera', 145, 58.4, 25.1, 1550, 'Kriya & Kuliner'),
    ('Bengkulu', 'Sumatera', 112, 56.2, 23.4, 1200, 'Kriya & Kuliner'),
    ('Kepulauan Bangka Belitung', 'Sumatera', 105, 59.1, 26.0, 1300, 'Kuliner & Kriya'),

    # Kalimantan
    ('Kalimantan Timur', 'Kalimantan', 280, 68.4, 35.8, 3800, 'Kriya & Kuliner (IKN Buffer)'),
    ('Kalimantan Barat', 'Kalimantan', 198, 60.5, 27.4, 2100, 'Kriya & Kuliner'),
    ('Kalimantan Selatan', 'Kalimantan', 186, 61.8, 28.6, 2050, 'Kriya (Sasirangan) & Kuliner'),
    ('Kalimantan Tengah', 'Kalimantan', 125, 57.2, 24.2, 1350, 'Kriya Rotan & Kuliner'),
    ('Kalimantan Utara', 'Kalimantan', 74, 55.4, 22.0, 850, 'Kuliner & Kriya'),

    # Sulawesi
    ('Sulawesi Selatan', 'Sulawesi', 345, 66.8, 33.5, 3950, 'Kuliner & Fesyen (Sutera)'),
    ('Sulawesi Utara', 'Sulawesi', 192, 64.5, 31.0, 2200, 'Kuliner & Musik'),
    ('Sulawesi Tengah', 'Sulawesi', 138, 57.8, 24.8, 1450, 'Kriya & Kuliner'),
    ('Sulawesi Tenggara', 'Sulawesi', 122, 56.4, 23.5, 1300, 'Kriya & Kuliner'),
    ('Gorontalo', 'Sulawesi', 88, 56.0, 22.8, 920, 'Kriya (Karawo) & Kuliner'),
    ('Sulawesi Barat', 'Sulawesi', 72, 53.2, 21.0, 780, 'Kriya (Tenun) & Kuliner'),

    # Maluku & Papua
    ('Maluku', 'Maluku & Papua', 95, 55.8, 22.4, 980, 'Musik & Kuliner (Rempah)'),
    ('Maluku Utara', 'Maluku & Papua', 78, 54.2, 21.5, 820, 'Kuliner & Kriya'),
    ('Papua', 'Maluku & Papua', 115, 56.5, 23.0, 1250, 'Kriya (Noken) & Kesenian'),
    ('Papua Barat', 'Maluku & Papua', 76, 54.8, 21.8, 800, 'Kriya & Ekowisata'),
    ('Papua Barat Daya', 'Maluku & Papua', 68, 55.1, 22.2, 750, 'Kriya & Kuliner'),
    ('Papua Tengah', 'Maluku & Papua', 54, 50.2, 18.5, 580, 'Kriya Tradisional'),
    ('Papua Pegunungan', 'Maluku & Papua', 42, 48.5, 16.8, 450, 'Kriya Tradisional'),
    ('Papua Selatan', 'Maluku & Papua', 48, 51.0, 19.2, 520, 'Kriya & Kuliner')
]

data_prov_rows = []
total_prov_sample = sum(p[2] for p in provinsi_data)

for p in provinsi_data:
    prov_name, region, sample_hub, ev_dci, pct_ecommerce, kredit_miliar, unggulan = p
    est_pelaku_prov = int(sample_hub * (8500000 / total_prov_sample))
    data_prov_rows.append({
        'Provinsi': prov_name,
        'Wilayah_Pulau': region,
        'Pelaku_Sampel_Hub': sample_hub,
        'Estimasi_Pelaku_Daerah': est_pelaku_prov,
        'Porsi_Pelaku_Persen': round((sample_hub / total_prov_sample) * 100, 2),
        'Indeks_Daya_Saing_Digital (EV-DCI)': ev_dci,
        'Adopsi_ECommerce_Persen': pct_ecommerce,
        'Penyaluran_Pembiayaan_Miliar_IDR': kredit_miliar,
        'Subsektor_Unggulan': unggulan,
        'Kategori_Wilayah': 'Jawa (Hub Utama)' if region == 'Jawa' else 'Luar Jawa (Wilayah Berkembang)'
    })

df_provinsi = pd.DataFrame(data_prov_rows)
df_provinsi.to_csv("d:/final-project-ekraf/data/dataset_provinsi_ekraf.csv", index=False)
print("Saved dataset_provinsi_ekraf.csv")

# ==============================================================================
# 4. TABEL MIKRO / RESPONDEN EKRAF HUB (10,478 Baris - Sesuai Data Slide 6)
# ==============================================================================
# Slide 6 specifies:
# Total: 10,478
# Status Pengguna: Pemilik Usaha: 6,323, Umum: 2,767, Pekerja Kreatif: 1,321, Asosiasi: 67
# Let's generate the exact 10,478 individual records!

N = 10478
statuses = (
    ['Pemilik Usaha'] * 6323 +
    ['Umum'] * 2767 +
    ['Pekerja Kreatif'] * 1321 +
    ['Asosiasi'] * 67
)
np.random.shuffle(statuses)

# Sample subsectors based on weights
sub_prob = [count / sum(jumlah_pelaku_hub) for count in jumlah_pelaku_hub]
sampled_subsectors = np.random.choice(subsektor_names, size=N, p=sub_prob)

# Sample provinces based on weights
prov_names = [p[0] for p in provinsi_data]
prov_counts = [p[2] for p in provinsi_data]
prov_prob = [c / sum(prov_counts) for c in prov_counts]
sampled_provinces = np.random.choice(prov_names, size=N, p=prov_prob)

# Map province to region
prov_to_region = {p[0]: p[1] for p in provinsi_data}
sampled_regions = [prov_to_region[p] for p in sampled_provinces]

# Digital Adoption levels
# Tech/Digital subsectors have higher full-digital rate
skala_usaha_choices = ['Mikro', 'Kecil', 'Menengah']
skala_usaha_prob = [0.82, 0.15, 0.03]
sampled_skala = np.random.choice(skala_usaha_choices, size=N, p=skala_usaha_prob)

digital_status = []
omzet_bulanan = []
tenaga_kerja = []
fintech_user = []
impact_revenue = []
sumber_modal = []

modal_options = ['Modal Sendiri / Tabungan', 'Pinjaman Bank (KUR)', 'Fintech P2P / Pembiayaan Digital', 'Koperasi / Teman', 'Bantuan Pemerintah']
modal_prob = [0.58, 0.22, 0.12, 0.05, 0.03]

for i in range(N):
    sub = sampled_subsectors[i]
    reg = sampled_regions[i]
    skala = sampled_skala[i]
    
    # Base probability for digital adoption
    is_tech = sub in ['Aplikasi', 'Permainan (Game)', 'Desain Komunikasi Visual', 'Film, Animasi dan Video']
    is_jawa = reg == 'Jawa'
    
    p_full = 0.55 if is_tech else (0.35 if is_jawa else 0.22)
    p_social = 0.35 if is_tech else 0.45
    p_offline = max(0.02, 1.0 - p_full - p_social)
    
    dig = np.random.choice(['Full Digital (Marketplace & POS)', 'Media Sosial Saja', 'Offline / Belum Digital'], 
                           p=[p_full, p_social, p_offline])
    digital_status.append(dig)
    
    # Fintech user
    p_fintech = 0.58 if dig == 'Full Digital (Marketplace & POS)' else (0.28 if dig == 'Media Sosial Saja' else 0.08)
    uses_fintech = 'Ya' if np.random.rand() < p_fintech else 'Tidak'
    fintech_user.append(uses_fintech)
    
    # Sumber Modal
    if uses_fintech == 'Ya' and np.random.rand() < 0.4:
        modal = 'Fintech P2P / Pembiayaan Digital'
    else:
        modal = np.random.choice(modal_options, p=modal_prob)
    sumber_modal.append(modal)
    
    # Impact on revenue (Slide 5: 76.96% mitra amartha/digital mengalami kenaikan pendapatan!)
    if dig == 'Full Digital (Marketplace & POS)' or uses_fintech == 'Ya':
        p_impact = [0.42, 0.38, 0.15, 0.05] # Naik >30%, Naik 10-30%, Tetap, Turun
    elif dig == 'Media Sosial Saja':
        p_impact = [0.18, 0.45, 0.28, 0.09]
    else:
        p_impact = [0.05, 0.20, 0.52, 0.23]
    
    imp = np.random.choice(['Meningkat >30%', 'Meningkat 10-30%', 'Relatif Tetap (0-9%)', 'Mengalami Penurunan'], p=p_impact)
    impact_revenue.append(imp)
    
    # Omzet Bulanan (Juta IDR)
    if skala == 'Mikro':
        base_omzet = np.random.lognormal(mean=2.5, sigma=0.5) # approx 10 - 25 juta
        base_naker = np.random.choice([1, 2, 3, 4], p=[0.45, 0.35, 0.15, 0.05])
    elif skala == 'Kecil':
        base_omzet = np.random.lognormal(mean=4.2, sigma=0.4) # approx 50 - 150 juta
        base_naker = np.random.choice([5, 8, 12, 15], p=[0.4, 0.3, 0.2, 0.1])
    else: # Menengah
        base_omzet = np.random.lognormal(mean=5.8, sigma=0.3) # approx 250 - 600 juta
        base_naker = np.random.choice([20, 35, 50, 75], p=[0.4, 0.3, 0.2, 0.1])
        
    # Digital bonus
    if dig == 'Full Digital (Marketplace & POS)':
        base_omzet *= 1.35
    elif dig == 'Media Sosial Saja':
        base_omzet *= 1.12
        
    omzet_bulanan.append(round(base_omzet, 1))
    tenaga_kerja.append(int(base_naker))

df_mikro = pd.DataFrame({
    'ID_Pengguna': [f"EKRAF-{20260000 + i + 1}" for i in range(N)],
    'Status_Pengguna': statuses,
    'Subsektor': sampled_subsectors,
    'Provinsi': sampled_provinces,
    'Wilayah_Pulau': sampled_regions,
    'Skala_Usaha': sampled_skala,
    'Tingkat_Digitalisasi': digital_status,
    'Menggunakan_Fintech_Digital': fintech_user,
    'Sumber_Permodalan_Utama': sumber_modal,
    'Dampak_Digital_Thdp_Omzet': impact_revenue,
    'Omzet_Bulanan_Juta_IDR': omzet_bulanan,
    'Jumlah_Tenaga_Kerja': tenaga_kerja
})

df_mikro.to_csv("d:/final-project-ekraf/data/dataset_responden_ekraf_hub_10478.csv", index=False)
print("Saved dataset_responden_ekraf_hub_10478.csv")

# ==============================================================================
# 5. EXPORT MASTER EXCEL MULTI-SHEET FOR POWER BI ONE-CLICK IMPORT
# ==============================================================================
excel_path = "d:/final-project-ekraf/data/final_project_ekraf_master_data.xlsx"
with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    df_nasional.to_excel(writer, sheet_name='Tren_Nasional', index=False)
    df_subsektor.to_excel(writer, sheet_name='Subsektor_Ekraf', index=False)
    df_provinsi.to_excel(writer, sheet_name='Provinsi_Ekraf', index=False)
    df_mikro.to_excel(writer, sheet_name='Data_Responden_Hub', index=False)

print(f"Master Excel generated successfully at: {excel_path}")
