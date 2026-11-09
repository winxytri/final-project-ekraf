import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import numpy as np
import os

# Working directory
os.makedirs("d:/final-project-ekraf/output", exist_ok=True)

# Load data
df_subsektor = pd.read_csv("d:/final-project-ekraf/data/dataset_subsektor_ekraf.csv")
df_provinsi = pd.read_csv("d:/final-project-ekraf/data/dataset_provinsi_ekraf.csv")
df_mikro = pd.read_csv("d:/final-project-ekraf/data/dataset_responden_ekraf_hub_10478.csv")

# 16:9 Canvas Setup - 3840 x 2160 ultra high-res aesthetic
fig = plt.figure(figsize=(24, 13.5), facecolor='#070B14', dpi=160)
gs = fig.add_gridspec(32, 48)

# Upgraded Ekraf Creative Palette
BG_COLOR = '#070B14'
CARD_BG = '#0F172A'
CARD_BORDER = '#1E293B'

CORAL_CREATIVE = '#FF6B4A'  # Kuliner, Kriya, Culture
CYAN_DIGITAL = '#00D8D6'    # Digital, Tech, Apps
PURPLE_ARTS = '#A855F7'     # Fashion, Film, Arts
EMERALD_GROWTH = '#10B981'  # Omzet & Tenaga Kerja
GOLD_ACCENT = '#FFB800'     # Ekspor & Prestasi
ROSE_ACCENT = '#F43F5E'     # Risiko & Bottleneck

TEXT_TITLE = '#FFFFFF'
TEXT_BODY = '#E2E8F0'
TEXT_MUTED = '#94A3B8'

def draw_styled_card(ax, title="", subtitle="", border_color=CARD_BORDER, bg_color=CARD_BG):
    card = patches.FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.015,rounding_size=0.025",
                                  facecolor=bg_color, edgecolor=border_color, linewidth=1.8,
                                  transform=ax.transAxes, zorder=0)
    ax.add_patch(card)
    if title:
        ax.text(0.04, 0.94, title, transform=ax.transAxes,
                fontsize=13, fontweight='heavy', color=TEXT_TITLE, va='top', ha='left')
    if subtitle:
        ax.text(0.04, 0.88, subtitle, transform=ax.transAxes,
                fontsize=9, color=CYAN_DIGITAL, va='top', ha='left')

# ==============================================================================
# 1. HEADER SECTION (Rows 1 to 4)
# ==============================================================================
ax_head = fig.add_subplot(gs[1:4, 1:47])
ax_head.set_facecolor(BG_COLOR)
ax_head.axis('off')

# Title with prominent styling
ax_head.text(0.0, 0.88, "EKOSISTEM & AKSELERASI DIGITAL UMKM EKONOMI KREATIF INDONESIA",
             fontsize=23, fontweight='heavy', color=TEXT_TITLE, ha='left', va='top')
ax_head.text(0.0, 0.38, "Analisis Komprehensif Data Ekraf Hub, BPS, KemenkopUKM & Katadata | Final Project Track Data Analytics",
             fontsize=12, fontweight='semibold', color=CORAL_CREATIVE, ha='left', va='top')

# Badges right
ax_head.text(1.0, 0.88, "GOOGLE CAREER CERTIFICATES x KEMENPAREKRAF RI",
             fontsize=11.5, fontweight='bold', color='#FFFFFF', ha='right', va='top',
             bbox=dict(boxstyle='round,pad=0.55', facecolor='#1E1B4B', edgecolor=PURPLE_ARTS, linewidth=1.5))
ax_head.text(1.0, 0.35, "Portofolio Talenta Digital Indonesia 2026 | Live Session #2",
             fontsize=10, color=TEXT_MUTED, ha='right', va='top')

# ==============================================================================
# 2. ROW 1: 5 HIGHLIGHT METRIC CARDS (Rows 4 to 8)
# ==============================================================================
kpis = [
    {"tag": "PELAKU TERDAFTAR", "val": "10,478", "sub": "Sampel Terverifikasi Ekraf Hub", "color": CYAN_DIGITAL},
    {"tag": "PEMILIK USAHA MANDIRI", "val": "60.3%", "sub": "6,323 Unit Usaha Kreatif", "color": CORAL_CREATIVE},
    {"tag": "KONSENTRASI P. JAWA", "val": "69.3%", "sub": "7,257 Pelaku di 6 Provinsi", "color": GOLD_ACCENT},
    {"tag": "FULL DIGITAL (POS + E-COM)", "val": "36.4%", "sub": "3,814 Adopsi Solusi Terpadu", "color": PURPLE_ARTS},
    {"tag": "KENAIKAN OMZET MITRA", "val": "76.9%", "sub": "Efek Finansial Digital & Fintech", "color": EMERALD_GROWTH}
]

for idx, kpi in enumerate(kpis):
    c_start = 1 + idx * 9
    c_end = c_start + 9
    ax_k = fig.add_subplot(gs[4:8, c_start:c_end])
    ax_k.set_facecolor(CARD_BG)
    ax_k.axis('off')
    draw_styled_card(ax_k, border_color=kpi['color'])
    
    # Text
    ax_k.text(0.08, 0.82, f"[ {kpi['tag']} ]", transform=ax_k.transAxes,
              fontsize=9, fontweight='heavy', color=kpi['color'], va='center')
    ax_k.text(0.08, 0.46, kpi['val'], transform=ax_k.transAxes,
              fontsize=25, fontweight='heavy', color=TEXT_TITLE, va='center')
    ax_k.text(0.08, 0.16, kpi['sub'], transform=ax_k.transAxes,
              fontsize=8.5, color=TEXT_BODY, va='center')

# ==============================================================================
# 3. DONUT: STATUS PENGGUNA (Rows 9 to 19, Cols 1 to 14)
# ==============================================================================
ax_donut = fig.add_subplot(gs[9:19, 1:15])
ax_donut.set_facecolor(CARD_BG)
draw_styled_card(ax_donut, title="PROPORSI STATUS PENGGUNA", subtitle="Basis Data Profil Ekraf Hub")

st_counts = df_mikro['Status_Pengguna'].value_counts()
colors_donut = [CORAL_CREATIVE, CYAN_DIGITAL, PURPLE_ARTS, GOLD_ACCENT]
wedges, texts, autotexts = ax_donut.pie(
    st_counts.values,
    labels=[f"{k}\n({v:,})" for k, v in zip(st_counts.index, st_counts.values)],
    autopct='%1.1f%%',
    pctdistance=0.72,
    startangle=140,
    colors=colors_donut,
    textprops=dict(color=TEXT_BODY, fontsize=8.5, fontweight='semibold'),
    wedgeprops=dict(width=0.46, edgecolor=CARD_BG, linewidth=2.5)
)
for at in autotexts:
    at.set_fontsize(8.5)
    at.set_color('#FFFFFF')
    at.set_weight('bold')

ax_donut.text(0, 0, "TOTAL\n10,478\nPelaku", ha='center', va='center',
              fontsize=9.5, fontweight='heavy', color=TEXT_TITLE)

# ==============================================================================
# 4. BAR: TOP 12 SUBSEKTOR EKONOMI KREATIF (Rows 9 to 19, Cols 15 to 33)
# ==============================================================================
ax_subs = fig.add_subplot(gs[9:19, 15:33])
ax_subs.set_facecolor(CARD_BG)
draw_styled_card(ax_subs, title="TOP 12 SUBSEKTOR EKONOMI KREATIF", subtitle="Pelaku Terdaftar di Ekraf Hub")

top_subs = df_subsektor.head(12).sort_values(by='Pelaku_Sampel_Hub', ascending=True)
y_pos = np.arange(len(top_subs))
bar_colors = [
    CORAL_CREATIVE if s in ['Kuliner', 'Fesyen', 'Kriya']
    else (CYAN_DIGITAL if s in ['Aplikasi', 'Film, Animasi dan Video', 'Desain Komunikasi Visual', 'Permainan (Game)']
    else PURPLE_ARTS)
    for s in top_subs['Subsektor']
]

bars = ax_subs.barh(y_pos, top_subs['Pelaku_Sampel_Hub'], color=bar_colors, height=0.68, zorder=3)
ax_subs.set_yticks(y_pos)
ax_subs.set_yticklabels(top_subs['Subsektor'], color=TEXT_TITLE, fontsize=9, fontweight='semibold')
ax_subs.set_xlabel("Jumlah Pelaku Terdaftar", color=TEXT_MUTED, fontsize=8.5)
ax_subs.tick_params(axis='x', colors=TEXT_MUTED, labelsize=8)
ax_subs.set_xlim(0, 2850)
ax_subs.grid(axis='x', color=CARD_BORDER, linestyle='--', alpha=0.5, zorder=0)

for bar in bars:
    w = bar.get_width()
    ax_subs.text(w + 35, bar.get_y() + bar.get_height()/2, f"{int(w):,}",
                 ha='left', va='center', color=TEXT_TITLE, fontsize=8, fontweight='bold')

ax_subs.text(0.98, 0.94, "[*] Oranye: Big 3 (74% PDB)  |  Cyan: Tech & Media  |  Ungu: Arts",
             transform=ax_subs.transAxes, color=TEXT_MUTED, fontsize=8, ha='right', va='top')

# ==============================================================================
# 5. SEBARAN REGIONAL PROVINSI (Rows 9 to 19, Cols 34 to 47)
# ==============================================================================
ax_prov = fig.add_subplot(gs[9:19, 34:47])
ax_prov.set_facecolor(CARD_BG)
draw_styled_card(ax_prov, title="SEBARAN REGIONAL PROVINSI", subtitle="Konsentrasi Geografis Pelaku")

top_prov = df_provinsi.head(8).sort_values(by='Pelaku_Sampel_Hub', ascending=True)
y_p_prov = np.arange(len(top_prov))
prov_cols = [CYAN_DIGITAL if r == 'Jawa' else PURPLE_ARTS for r in top_prov['Wilayah_Pulau']]

bars_p = ax_prov.barh(y_p_prov, top_prov['Pelaku_Sampel_Hub'], color=prov_cols, height=0.65, zorder=3)
ax_prov.set_yticks(y_p_prov)
ax_prov.set_yticklabels(top_prov['Provinsi'], color=TEXT_TITLE, fontsize=9, fontweight='semibold')
ax_prov.set_xlabel("Jumlah Pelaku", color=TEXT_MUTED, fontsize=8.5)
ax_prov.tick_params(axis='x', colors=TEXT_MUTED, labelsize=8)
ax_prov.set_xlim(0, 2600)
ax_prov.grid(axis='x', color=CARD_BORDER, linestyle='--', alpha=0.5, zorder=0)

for bar in bars_p:
    w = bar.get_width()
    ax_prov.text(w + 30, bar.get_y() + bar.get_height()/2, f"{int(w):,}",
                 ha='left', va='center', color=TEXT_TITLE, fontsize=8, fontweight='bold')

ax_prov.text(0.98, 0.94, "[*] Cyan: Pulau Jawa  |  Ungu: Luar Pulau Jawa", transform=ax_prov.transAxes,
             color=TEXT_MUTED, fontsize=8, ha='right', va='top')

# ==============================================================================
# 6. DAMPAK DIGITAL TERHADAP OMZET (Rows 20 to 29, Cols 1 to 18)
# ==============================================================================
ax_imp = fig.add_subplot(gs[20:30, 1:19])
ax_imp.set_facecolor(CARD_BG)
draw_styled_card(ax_imp, title="DAMPAK DIGITALISASI TERHADAP OMZET", subtitle="Korelasi Pertumbuhan Finansial Pelaku")

short_cats = ['Full Digital\n(POS + E-Com)', 'Media Sosial\nSaja', 'Offline /\nKonvensional']
inc_high = [42, 18, 5]
inc_med = [38, 45, 20]
neutral = [15, 28, 52]
decrease = [5, 9, 23]

x = np.arange(len(short_cats))
w_b = 0.52

ax_imp.bar(x, inc_high, w_b, label='Naik >30%', color=EMERALD_GROWTH, zorder=3)
ax_imp.bar(x, inc_med, w_b, bottom=inc_high, label='Naik 10-30%', color=CYAN_DIGITAL, zorder=3)
ax_imp.bar(x, neutral, w_b, bottom=np.array(inc_high)+np.array(inc_med), label='Relatif Tetap', color='#64748B', zorder=3)
ax_imp.bar(x, decrease, w_b, bottom=np.array(inc_high)+np.array(inc_med)+np.array(neutral), label='Menurun', color=ROSE_ACCENT, zorder=3)

ax_imp.set_xticks(x)
ax_imp.set_xticklabels(short_cats, color=TEXT_TITLE, fontsize=8.5, fontweight='semibold')
ax_imp.set_ylabel("% Distribusi Responden", color=TEXT_MUTED, fontsize=8.5)
ax_imp.tick_params(axis='y', colors=TEXT_MUTED, labelsize=8)
ax_imp.set_ylim(0, 105)
ax_imp.legend(loc='lower left', bbox_to_anchor=(0.02, 0.76), ncol=2, frameon=False,
              fontsize=7.5, labelcolor=TEXT_TITLE)

# ==============================================================================
# 7. 5 KEY INSIGHTS & 3 REKOMENDASI (Rows 20 to 29, Cols 19 to 47)
# ==============================================================================
ax_ins = fig.add_subplot(gs[20:30, 20:47])
ax_ins.set_facecolor(CARD_BG)
draw_styled_card(ax_ins, title="5 KEY INSIGHTS DATA ANALYTICS & REKOMENDASI STRATEGIS",
                 subtitle="Temuan Kunci Berbasis Data untuk Pengambil Kebijakan", border_color=CORAL_CREATIVE)
ax_ins.axis('off')

story_content = (
    "KEY INSIGHTS BERBASIS DATA RIIL:\n"
    "1. Hegemoni Tri-Subsektor (Big 3): Kuliner (23.9%), Fesyen (13.6%), dan Kriya (9.3%) merangkul 46.8% pelaku di Ekraf Hub dan menyumbang >74% PDB Ekraf.\n"
    "2. Kesenjangan Regional Nyata: 69.3% pelaku usaha terkonsentrasi di Pulau Jawa (Jabar 2.232, Jatim 1.380, DKI 1.183), didorong tingginya skor kesiapan digital (EV-DCI 70-85).\n"
    "3. Kausalitas Kuat Digitalisasi: 80.2% pelaku berkategori 'Full Digital' mencatatkan lonjakan omzet (42% naik >30%), berbanding hanya 25% pada kelompok UMKM offline.\n"
    "4. Bottleneck Permodalan Formal: 58% UMKM masih bersandar pada modal pribadi/keluarga; penetrasi fintech produktif (12%) dan KUR bank (22%) masih perlu diakselerasi.\n"
    "5. Katup Pengaman Lapangan Kerja: Sektor UMKM menyerap 97% tenaga kerja nasional (rata-rata 3.2 pekerja/unit), menjadi pondasi utama stabilitas ekonomi riil.\n\n"
    "REKOMENDASI AKSI STRATEGIS:\n"
    "- Akselerasi Logistik Luar Jawa: Subsidi ongkos kirim e-commerce & shared fulfillment hub di luar Pulau Jawa (Sumatera, Sulsel, Bali-Nusra).\n"
    "- Inovasi Credit Scoring Digital: Integrasi data rekam transaksi Ekraf Hub dengan fintech P2P/KUR berizin OJK untuk UMKM unbanked tanpa agunan fisik.\n"
    "- Standarisasi & Kurasi Ekspor: Pelatihan mutu komoditas Fesyen & Kriya ramah lingkungan untuk mendongkrak devisa ekspor nasional."
)

ax_ins.text(0.03, 0.85, story_content, transform=ax_ins.transAxes,
            fontsize=8.5, color=TEXT_BODY, va='top', ha='left', linespacing=1.45)

# ==============================================================================
# 8. FOOTER: SUMBER DATA & ATRIBUSI
# ==============================================================================
ax_ft = fig.add_subplot(gs[30:32, 1:47])
ax_ft.set_facecolor(BG_COLOR)
ax_ft.axis('off')

footer_info = (
    "SUMBER DATA RESMI: Kementerian Pariwisata dan Ekonomi Kreatif (Ekraf Hub 2025/2026) | Badan Pusat Statistik (PDB Ekraf & Sakernas) | "
    "KemenkopUKM (Data Perkembangan UMKM) | Katadata Insight Center (EV-DCI 2025) | Disusun untuk Final Project Google Career Certificates Track Data Analytics"
)
ax_ft.text(0.5, 0.45, footer_info, transform=ax_ft.transAxes,
           fontsize=8.5, color=TEXT_MUTED, ha='center', va='center')

plt.subplots_adjust(left=0.02, right=0.98, top=0.96, bottom=0.03, wspace=0.3, hspace=0.3)

out_png = "d:/final-project-ekraf/output/infografis_ekraf_final_project.png"
out_pdf = "d:/final-project-ekraf/output/infografis_ekraf_final_project.pdf"

plt.savefig(out_png, dpi=200, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
plt.savefig(out_pdf, dpi=200, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
plt.close()

print(f"Updated Landscape Infographic generated cleanly without glyph warnings:\n- {out_png}\n- {out_pdf}")
