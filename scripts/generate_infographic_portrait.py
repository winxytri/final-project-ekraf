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

# Canvas setup - High-Res Portrait Poster (1200 x 2000 px approx)
fig = plt.figure(figsize=(12, 20), facecolor='#070B14', dpi=160)
gs = fig.add_gridspec(48, 24)

# Colors
BG_COLOR = '#070B14'
CARD_BG = '#0F172A'
CARD_BORDER = '#1E293B'

CORAL_CREATIVE = '#FF6B4A'
CYAN_DIGITAL = '#00D8D6'
PURPLE_ARTS = '#A855F7'
EMERALD_GROWTH = '#10B981'
GOLD_ACCENT = '#FFB800'

TEXT_TITLE = '#FFFFFF'
TEXT_BODY = '#E2E8F0'
TEXT_MUTED = '#94A3B8'

def draw_card(ax, title="", border_color=CARD_BORDER):
    card = patches.FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.015,rounding_size=0.025",
                                  facecolor=CARD_BG, edgecolor=border_color, linewidth=1.6,
                                  transform=ax.transAxes, zorder=0)
    ax.add_patch(card)
    if title:
        ax.text(0.04, 0.94, title, transform=ax.transAxes,
                fontsize=11.5, fontweight='heavy', color=TEXT_TITLE, va='top', ha='left')

# 1. HEADER (Rows 1 to 4)
ax_head = fig.add_subplot(gs[1:5, 1:23])
ax_head.set_facecolor(BG_COLOR)
ax_head.axis('off')

ax_head.text(0.5, 0.90, "BAGAIMANA UMKM EKRAF", fontsize=21, fontweight='heavy',
             color=TEXT_TITLE, ha='center', va='top')
ax_head.text(0.5, 0.63, "MENDORONG PERTUMBUHAN EKONOMI DAERAH?", fontsize=16, fontweight='heavy',
             color=CORAL_CREATIVE, ha='center', va='top')
ax_head.text(0.5, 0.30, "Analisis Integrasi Data Ekraf Hub, BPS, KemenkopUKM & Katadata",
             fontsize=10.5, color=CYAN_DIGITAL, ha='center', va='top')
ax_head.text(0.5, 0.06, "Google Career Certificates x Kementerian Ekonomi Kreatif RI",
             fontsize=9, color=TEXT_MUTED, ha='center', va='top')

# 2. MACRO STATS (Rows 5 to 9)
ax_macro = fig.add_subplot(gs[5:10, 1:23])
ax_macro.set_facecolor(CARD_BG)
draw_card(ax_macro, title="PENGGERAK PEREKONOMIAN NASIONAL", border_color=CORAL_CREATIVE)
ax_macro.axis('off')

macro_boxes = [
    {"label": "Serapan Tenaga Kerja", "val": "97%", "sub": "125.2 Juta Jiwa", "col": 0.05, "c": CYAN_DIGITAL},
    {"label": "Kontribusi PDB", "val": "62%", "sub": "Rp 14.620 Triliun", "col": 0.30, "c": CORAL_CREATIVE},
    {"label": "Populasi UMKM", "val": "65.5 Jt", "sub": "Unit Usaha Nasional", "col": 0.55, "c": PURPLE_ARTS},
    {"label": "Potensi Bisnis", "val": "Rp 2.194 T", "sub": "Perputaran Ekonomi", "col": 0.80, "c": EMERALD_GROWTH}
]
for mb in macro_boxes:
    ax_macro.text(mb['col'], 0.65, mb['val'], transform=ax_macro.transAxes,
                  fontsize=18, fontweight='heavy', color=mb['c'], ha='left', va='center')
    ax_macro.text(mb['col'], 0.38, mb['label'], transform=ax_macro.transAxes,
                  fontsize=9, fontweight='bold', color=TEXT_TITLE, ha='left', va='center')
    ax_macro.text(mb['col'], 0.18, mb['sub'], transform=ax_macro.transAxes,
                  fontsize=8, color=TEXT_MUTED, ha='left', va='center')

# 3. DONUT STATUS & SUBSEKTOR BAR (Rows 10 to 20)
ax_st = fig.add_subplot(gs[11:21, 1:11])
ax_st.set_facecolor(CARD_BG)
draw_card(ax_st, title="PROPORSI STATUS PELAKU")

st_counts = df_mikro['Status_Pengguna'].value_counts()
ax_st.pie(
    st_counts.values,
    labels=[f"{k}\n({v:,})" for k, v in zip(st_counts.index, st_counts.values)],
    autopct='%1.0f%%',
    pctdistance=0.70,
    startangle=140,
    colors=[CORAL_CREATIVE, CYAN_DIGITAL, PURPLE_ARTS, GOLD_ACCENT],
    textprops=dict(color=TEXT_TITLE, fontsize=7.5, fontweight='semibold'),
    wedgeprops=dict(width=0.45, edgecolor=CARD_BG, linewidth=2)
)
ax_st.text(0, 0, "10,478\nPelaku", ha='center', va='center', fontsize=8.5, fontweight='heavy', color=TEXT_TITLE)

# Subsektor Bar
ax_sb = fig.add_subplot(gs[11:21, 12:23])
ax_sb.set_facecolor(CARD_BG)
draw_card(ax_sb, title="TOP SUBSEKTOR EKRAF")

top_subs = df_subsektor.head(8).sort_values(by='Pelaku_Sampel_Hub', ascending=True)
y_p = np.arange(len(top_subs))
b_cols = [CORAL_CREATIVE if s in ['Kuliner', 'Fesyen', 'Kriya'] else CYAN_DIGITAL for s in top_subs['Subsektor']]
bars = ax_sb.barh(y_p, top_subs['Pelaku_Sampel_Hub'], color=b_cols, height=0.65, zorder=3)
ax_sb.set_yticks(y_p)
ax_sb.set_yticklabels(top_subs['Subsektor'], color=TEXT_TITLE, fontsize=8, fontweight='semibold')
ax_sb.tick_params(axis='x', colors=TEXT_MUTED, labelsize=7.5)
ax_sb.grid(axis='x', color=CARD_BORDER, linestyle='--', alpha=0.5, zorder=0)
for bar in bars:
    w = bar.get_width()
    ax_sb.text(w + 30, bar.get_y() + bar.get_height()/2, f"{int(w):,}",
               ha='left', va='center', color=TEXT_TITLE, fontsize=7.5, fontweight='bold')

# 4. DAMPAK DIGITAL & PEMBIAYAAN (Rows 22 to 31)
ax_pil = fig.add_subplot(gs[22:31, 1:23])
ax_pil.set_facecolor(CARD_BG)
draw_card(ax_pil, title="TRANSFORMASI DIGITAL & PEMBIAYAAN PRODUKTIF", border_color=CYAN_DIGITAL)
ax_pil.axis('off')

stats_pilar = [
    ("76.96%", "Mitra Alami Kenaikan Omzet", "Dampak nyata teknologi & permodalan"),
    ("50.000+", "UMKM Berhasil Naik Kelas", "Transformasi dari mikro ke kecil/menengah"),
    ("36.4%", "Pelaku Full Digital", "Marketplace + POS Kasir Terpadu"),
    ("69.3%", "Konsentrasi Pulau Jawa", "Disparitas digital daerah perlu diratakan")
]
for i, sp in enumerate(stats_pilar):
    x_pos = 0.05 if i % 2 == 0 else 0.55
    y_pos = 0.68 if i < 2 else 0.32
    ax_pil.text(x_pos, y_pos, sp[0], transform=ax_pil.transAxes,
                fontsize=18, fontweight='heavy',
                color=EMERALD_GROWTH if i == 0 else (CORAL_CREATIVE if i == 1 else CYAN_DIGITAL))
    ax_pil.text(x_pos + 0.18, y_pos + 0.04, sp[1], transform=ax_pil.transAxes,
                fontsize=9.5, fontweight='bold', color=TEXT_TITLE)
    ax_pil.text(x_pos + 0.18, y_pos - 0.05, sp[2], transform=ax_pil.transAxes,
                fontsize=8, color=TEXT_MUTED)

# 5. 5 KEY INSIGHTS (Rows 32 to 40)
ax_in = fig.add_subplot(gs[32:41, 1:23])
ax_in.set_facecolor(CARD_BG)
draw_card(ax_in, title="5 KEY INSIGHTS BERBASIS DATA RIIL")
ax_in.axis('off')

in_text = (
    "1. Dominasi Tri-Subsektor: Kuliner (23.9%), Fesyen (13.6%), dan Kriya (9.3%) kuasai 46.8% pelaku di Ekraf Hub.\n"
    "2. Kesenjangan Wilayah: 69.3% pelaku berada di Pulau Jawa (Jawa Barat 2.232, Jatim 1.380, DKI 1.183 pelaku).\n"
    "3. Efek Nyata Digitalisasi: 80.2% pelaku Full Digital mencatat kenaikan omzet vs hanya 25% pada pelaku offline.\n"
    "4. Penetrasi Permodalan: 58% UMKM masih modal sendiri, akses fintech produktif (12%) & KUR (22%) butuh digenjot.\n"
    "5. Penyerapan Tenaga Kerja: Sektor UMKM menyerap rata-rata 3.2 pekerja/unit, penopang stabilitas ekonomi riil."
)
ax_in.text(0.04, 0.85, in_text, transform=ax_in.transAxes,
           fontsize=8.5, color=TEXT_BODY, va='top', ha='left', linespacing=1.6)

# 6. REKOMENDASI STRATEGIS (Rows 41 to 45)
ax_rec = fig.add_subplot(gs[41:46, 1:23])
ax_rec.set_facecolor(CARD_BG)
draw_card(ax_rec, title="REKOMENDASI AKSI STRATEGIS", border_color=PURPLE_ARTS)
ax_rec.axis('off')

rec_text = (
    "• Akselerasi Logistik Luar Jawa: Subsidi ongkos kirim e-commerce & shared fulfillment hub luar Jawa.\n"
    "• Inovasi Credit Scoring Digital: Integrasi profil Ekraf Hub dengan fintech P2P dan KUR untuk UMKM unbanked.\n"
    "• Standardisasi & Kurasi Ekspor: Pelatihan mutu komoditas Fesyen & Kriya untuk tembus pasar global."
)
ax_rec.text(0.04, 0.82, rec_text, transform=ax_rec.transAxes,
           fontsize=8.5, color=TEXT_BODY, va='top', ha='left', linespacing=1.5)

# 7. FOOTER
ax_ft = fig.add_subplot(gs[46:48, 1:23])
ax_ft.set_facecolor(BG_COLOR)
ax_ft.axis('off')

ft = "SUMBER: Kemenparekraf (Ekraf Hub 2025/2026) | BPS (PDB & Sakernas) | KemenkopUKM | Katadata (EV-DCI)"
ax_ft.text(0.5, 0.5, ft, transform=ax_ft.transAxes,
           fontsize=8, color=TEXT_MUTED, ha='center', va='center')

plt.subplots_adjust(left=0.03, right=0.97, top=0.98, bottom=0.02, wspace=0.2, hspace=0.35)

out_portrait = "d:/final-project-ekraf/output/infografis_ekraf_portrait.png"
plt.savefig(out_portrait, dpi=200, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
plt.close()

print(f"Updated Portrait Infographic successfully generated at: {out_portrait}")
