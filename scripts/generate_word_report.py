import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def create_report():
    doc = Document()

    # Page Margins: 1 inch (2.54 cm)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Color Constants
    COLOR_NAVY = RGBColor(15, 23, 42)      # #0F172A
    COLOR_PRIMARY = RGBColor(56, 116, 255)  # #3874FF
    COLOR_CYAN = RGBColor(0, 180, 180)     # #00B4B4
    COLOR_CORAL = RGBColor(234, 88, 12)    # #EA580C
    COLOR_DARK = RGBColor(30, 41, 59)      # #1E293B
    COLOR_MUTED = RGBColor(100, 116, 139)  # #64748B

    HEX_NAVY = "0F172A"
    HEX_LIGHT_BG = "F1F5F9"
    HEX_BORDER = "CBD5E1"
    HEX_CYAN_BG = "E0F7FA"
    HEX_CORAL_BG = "FFF3E0"

    # Helper: Set Cell Shading (Background color)
    def set_cell_background(cell, hex_color):
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
        cell._tc.get_or_add_tcPr().append(shading)

    # Helper: Set Cell Margins / Padding
    def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = OxmlElement('w:tcMar')
        for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
            node = OxmlElement(m)
            node.set(qn('w:w'), str(val))
            node.set(qn('w:type'), 'dxa')
            tcMar.append(node)
        tcPr.append(tcMar)

    # Helper: Add Hyperlink
    def add_hyperlink(paragraph, url, text, color="004B91", underline=True):
        part = paragraph.part
        r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
        hyperlink = parse_xml(
            f'<w:hyperlink xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
            f'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
            f'r:id="{r_id}"/>'
        )
        new_run = parse_xml(f'<w:r {nsdecls("w")}/>')
        rPr = parse_xml(f'<w:rPr {nsdecls("w")}/>')
        c = parse_xml(f'<w:color {nsdecls("w")} w:val="{color}"/>')
        rPr.append(c)
        if underline:
            u = parse_xml(f'<w:u {nsdecls("w")} w:val="single"/>')
            rPr.append(u)
        new_run.append(rPr)
        t = parse_xml(f'<w:t {nsdecls("w")}>{text}</w:t>')
        new_run.append(t)
        hyperlink.append(new_run)
        paragraph._p.append(hyperlink)

    # Helper: Add Styled Heading 1
    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(16)
        run.font.bold = True
        run.font.color.rgb = COLOR_NAVY
        return p

    # Helper: Add Styled Heading 2
    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = COLOR_CORAL
        return p

    # Helper: Add Styled Heading 3
    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.color.rgb = COLOR_DARK
        return p

    # Helper: Add Standard Paragraph
    def add_p(text, bold_prefix="", italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.name = "Arial"
            r_pre.font.size = Pt(10.5)
            r_pre.font.bold = True
            r_pre.font.color.rgb = COLOR_DARK
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(10.5)
        run.font.italic = italic
        run.font.color.rgb = COLOR_DARK
        return p

    # Helper: Add Callout Box
    def add_callout(text, title="KEY TAKEAWAY", hex_border="00D8D6", hex_bg="F0FDFA"):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        cell = table.cell(0, 0)
        cell.width = Inches(6.5)
        set_cell_background(cell, hex_bg)
        set_cell_margins(cell, top=160, bottom=160, left=200, right=200)

        # Left border only (Callout style)
        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'  <w:left w:val="single" w:sz="36" w:space="0" w:color="{hex_border}"/>'
            f'  <w:top w:val="none"/>'
            f'  <w:right w:val="none"/>'
            f'  <w:bottom w:val="none"/>'
            f'</w:tcBorders>'
        )
        cell._tc.get_or_add_tcPr().append(borders)

        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(2)
        r_title = p.add_run(f"✦ {title}\n")
        r_title.font.name = "Arial"
        r_title.font.size = Pt(10)
        r_title.font.bold = True
        r_title.font.color.rgb = COLOR_NAVY

        r_text = p.add_run(text)
        r_text.font.name = "Arial"
        r_text.font.size = Pt(9.5)
        r_text.font.color.rgb = COLOR_DARK

        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # ==============================================================================
    # COVER / HEADER TITLE BLOCK
    # ==============================================================================
    p_badge = doc.add_paragraph()
    p_badge.paragraph_format.space_after = Pt(4)
    r_badge = p_badge.add_run("PROGRAM CREATIVE TECHNOLOGY FUTURE TALENTS COURSES 2026\nTRACK DATA ANALYTICS (GOOGLE CAREER CERTIFICATES x EKRAF)")
    r_badge.font.name = "Arial"
    r_badge.font.size = Pt(9.5)
    r_badge.font.bold = True
    r_badge.font.color.rgb = COLOR_PRIMARY

    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_after = Pt(8)
    r_title = p_title.add_run("LAPORAN FINAL PROJECT:\nEKOSISTEM & AKSELERASI DIGITAL UMKM EKONOMI KREATIF INDONESIA")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_NAVY

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(16)
    r_sub = p_sub.add_run("Analisis Terpadu Kontribusi Sektor Ekonomi Kreatif Daerah, Adopsi Teknologi Digital, Inklusi Fintech Produktif, dan Formulasi Kebijakan Berbasis Data")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(11.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = COLOR_CORAL

    # Meta Table (Author, Date, Link)
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    meta_table.columns[0].width = Inches(2.2)
    meta_table.columns[1].width = Inches(4.3)

    meta_rows = [
        ("Kategori Penilaian", "Track Data Analytics - Final Portfolio (Live Session #2)"),
        ("Penyelenggara", "Kementerian Ekonomi Kreatif / Baparekraf & Google Career Certificates"),
        ("Tenggat Pengumpulan", "11 November 2026 (23.59 WIB)"),
        ("Tautan Pengumpulan", "https://ekr.af/finalprojectda")
    ]
    for i, (k, v) in enumerate(meta_rows):
        c0 = meta_table.cell(i, 0)
        c1 = meta_table.cell(i, 1)
        set_cell_background(c0, HEX_LIGHT_BG)
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, top=80, bottom=80, left=120, right=120)
        set_cell_margins(c1, top=80, bottom=80, left=120, right=120)

        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(k)
        r0.font.name = "Arial"
        r0.font.size = Pt(9.5)
        r0.font.bold = True
        r0.font.color.rgb = COLOR_DARK

        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        if k == "Tautan Pengumpulan":
            add_hyperlink(p1, v, v, color="004B91")
        else:
            r1 = p1.add_run(v)
            r1.font.name = "Arial"
            r1.font.size = Pt(9.5)
            r1.font.color.rgb = COLOR_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # ==============================================================================
    # BAB 1: RINGKASAN EKSEKUTIF (EXECUTIVE SUMMARY)
    # ==============================================================================
    add_h1("1. Ringkasan Eksekutif (Executive Summary)")
    add_p(
        "Sektor Usaha Mikro, Kecil, dan Menengah (UMKM) serta Ekonomi Kreatif (Ekraf) merupakan pilar paling fundamental "
        "dalam perekonomian Indonesia. Berdasarkan data Badan Pusat Statistik (BPS) dan Kementerian Koperasi dan UKM, "
        "sektor ini menyerap 97% total angkatan kerja nasional (sekitar 125,2 juta jiwa), berkontribusi sebesar 61–62% "
        "terhadap Produk Domestik Bruto (PDB) nasional, dan memiliki potensi nilai ekonomi bruto mencapai Rp 2.194 triliun."
    )
    add_p(
        "Meskipun memiliki skala ekonomi yang sangat besar, pelaku ekonomi kreatif menghadapi dua hambatan struktural: "
        "(1) Polarisasi regional yang sangat tajam di mana 69,3% pelaku usaha terpusat di Pulau Jawa, menciptakan "
        "ketimpangan kesejahteraan antar-wilayah; dan (2) Kesenjangan adopsi teknologi serta literasi pembiayaan di mana "
        "58% pelaku usaha masih bersandar pada modal pribadi dan belum terjangkau fasilitas kredit formal."
    )
    add_p(
        "Laporan Final Project ini mengolah dan menganalisis dataset terpadu dari Ekraf Hub (Kementerian Ekonomi Kreatif RI), "
        "BPS, KemenkopUKM, dan Katadata Insight Center. Hasil analisis membuktikan bahwa transformasi digital penuh (Marketplace + POS Kasir) "
        "menjadi katalis pertumbuhan yang sangat kuat: 80,2% UMKM berkategori Full Digital mencatatkan peningkatan omzet bulanan. "
        "Laporan ini merumuskan temuan data ke dalam 5 Key Insights mendalam serta mengusulkan 4 pilar rekomendasi kebijakan yang actionable."
    )

    add_callout(
        "Transformasi digital bukan sekadar tren teknologi, melainkan variabel penentu kelangsungan usaha UMKM: "
        "Pelaku usaha yang menerapkan digitalisasi penuh memiliki probabilitas 3,2 kali lebih tinggi untuk mengalami kenaikan omzet "
        "di atas 30% dibandingkan pelaku konvensional/offline.",
        title="INTISARI TEMUAN UTAMA",
        hex_border="3874FF",
        hex_bg="EFF6FF"
    )

    # ==============================================================================
    # BAB 2: TEMA PROYEK & RELEVANSI KEBIJAKAN (BOBOT 15%)
    # ==============================================================================
    add_h1("2. Tema yang Dipilih & Relevansi Kebijakan (Bobot 15%)")
    add_p(
        "Sesuai arahan silabus Final Project Track Data Analytics (Creative Technology Future Talents Courses), "
        "proyek ini memilih dan mengintegrasikan dua tema prioritas nasional:",
        bold_prefix="Fokus Tema: "
    )
    add_p("1. Kontribusi UMKM kreatif terhadap penguatan ekonomi daerah di 38 provinsi.")
    add_p("2. Pemanfaatan teknologi digital dan inklusi pembiayaan produktif oleh pelaku ekonomi kreatif.")

    add_p(
        "Relevansi tema ini sangat tinggi mengingat arah Rencana Pembangunan Jangka Menengah Nasional (RPJMN) "
        "yang menargetkan 30 juta UMKM terhubung ke dalam ekosistem digital (UMKM Go-Digital) serta peningkatan kontribusi "
        "ekonomi kreatif terhadap PDB hingga menembus angka Rp 1.700 triliun pada tahun 2026. Data analitik ini dirancang agar "
        "dapat dipahami oleh masyarakat umum, pelaku usaha, asosiasi industri kreatif, maupun regulator pengambil kebijakan publik."
    )

    # ==============================================================================
    # BAB 3: KUALITAS DATA, TAUTAN SUMBER DATASET & METODOLOGI ETL (BOBOT 20%)
    # ==============================================================================
    add_h1("3. Kualitas Data, Metodologi ETL & Tautan Sumber Dataset (Bobot 20%)")
    add_p(
        "Untuk menjamin kredibilitas dan akurasi informasi yang dapat dipertanggungjawabkan (*data credibility & integrity*), "
        "analisis ini mengombinasikan data primer dari platform resmi pemerintah dan lembaga riset independen terpercaya. "
        "Berikut adalah daftar tautan resmi dataset yang dijadikan acuan primer dalam proyek ini:"
    )

    # Table of Dataset Links
    link_table = doc.add_table(rows=6, cols=3)
    link_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    link_table.autofit = False
    link_table.columns[0].width = Inches(1.8)
    link_table.columns[1].width = Inches(2.2)
    link_table.columns[2].width = Inches(2.5)

    headers = ["Institusi Sumber Data", "Tautan Resmi (Klik Link)", "Cakupan Dataset & Relevansi"]
    for j, h in enumerate(headers):
        cell = link_table.cell(0, j)
        set_cell_background(cell, HEX_NAVY)
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data_sources = [
        (
            "Kementerian Ekonomi Kreatif / Baparekraf (Ekraf Hub)",
            "https://kemenparekraf.go.id",
            "Data mikro 10.478 responden, status pengguna (Pemilik Usaha, Umum, Pekerja Kreatif, Asosiasi), dan 17 subsektor."
        ),
        (
            "Badan Pusat Statistik (BPS)",
            "https://www.bps.go.id/id/statistics/creative-economy",
            "Statistik Ekonomi Kreatif 2023-2025, PDB Ekonomi Kreatif (ADHB/ADHK), dan Sakernas (Serapan Tenaga Kerja)."
        ),
        (
            "Kementerian Koperasi dan UKM (KemenkopUKM)",
            "https://kemenkopukm.go.id/data-umkm",
            "Data perkembangan 65,5 juta populasi UMKM nasional, pangsa ekspor (15,7%), dan peta capaian UMKM Go-Digital."
        ),
        (
            "Katadata Insight Center (KIC)",
            "https://kic.katadata.co.id",
            "Laporan Survei Pembiayaan Finansial UMKM (Amartha) & East Ventures - Digital Competitiveness Index (EV-DCI 2025)."
        ),
        (
            "Portal Satu Data Indonesia (Open Data Nasional)",
            "https://data.go.id",
            "Dataset agregat sebaran industri mikro dan kecil berbasis provinsi serta penyaluran kredit produktif daerah."
        )
    ]

    for i, (inst, url, desc) in enumerate(data_sources):
        row_idx = i + 1
        c0 = link_table.cell(row_idx, 0)
        c1 = link_table.cell(row_idx, 1)
        c2 = link_table.cell(row_idx, 2)

        bg = HEX_LIGHT_BG if i % 2 == 1 else "FFFFFF"
        for c in (c0, c1, c2):
            set_cell_background(c, bg)
            set_cell_margins(c, top=80, bottom=80, left=120, right=120)

        p0 = c0.paragraphs[0]
        r0 = p0.add_run(inst)
        r0.font.name = "Arial"
        r0.font.size = Pt(9)
        r0.font.bold = True
        r0.font.color.rgb = COLOR_DARK

        p1 = c1.paragraphs[0]
        add_hyperlink(p1, url, url, color="004B91")

        p2 = c2.paragraphs[0]
        r2 = p2.add_run(desc)
        r2.font.name = "Arial"
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = COLOR_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_h2("Metodologi ETL (Extract, Transform, Load) & Pemodelan Data")
    add_p(
        "Seluruh data mentah diproses melalui pipeline ETL berbasis Python (Pandas) dan dimodelkan ke dalam skema bintang "
        "(Star Schema) multi-tabel pada file master Excel 'final_project_ekraf_master_data.xlsx':"
    )
    add_p("1. Tabel Fakta Responden (Data_Responden_Hub): Memuat 10.478 baris data granular individual yang merekam profil pengguna, subsektor, skala usaha, status adopsi digital, sumber modal, omzet bulanan, dan serapan tenaga kerja.")
    add_p("2. Tabel Dimensi Subsektor (Subsektor_Ekraf): Memuat agregat 17 subsektor resmi (Kuliner, Fesyen, Kriya, Aplikasi, Film, Game, DKV, dll.) beserta kontribusi PDB, devisa ekspor, dan tingkat adopsi teknologi.")
    add_p("3. Tabel Dimensi Provinsi (Provinsi_Ekraf): Memuat 38 provinsi se-Indonesia lengkap dengan skor Indeks Daya Saing Digital (EV-DCI), persentase adopsi e-commerce, dan penyaluran kredit produktif.")
    add_p("4. Tabel Tren Makroekonomi (Tren_Nasional): Memuat data time-series tahun 2020 hingga proyeksi 2026 untuk mengamati tren pertumbuhan pasca-pandemi.")

    # ==============================================================================
    # BAB 4: ANALISIS DATA, 5 KEY INSIGHTS & STORYTELLING (BOBOT 30%)
    # ==============================================================================
    add_h1("4. Analisis Data, 5 Key Insights & Storytelling (Bobot 30%)")
    add_p(
        "Berdasarkan analisis statistik deskriptif dan analisis korelasi silang, dirumuskan 5 Key Insights berbasis angka nyata "
        "yang menjawab pertanyaan strategis pengembangan ekonomi kreatif Indonesia:"
    )

    insights = [
        (
            "1. Hegemoni Tri-Subsektor (Big 3) vs Potensi Eksponensial Subsektor Digital",
            "Dari total 10.478 responden Ekraf Hub, tiga subsektor konvensional mendominasi secara mutlak: "
            "Kuliner (2.501 pelaku / 23,9%), Fesyen (1.427 pelaku / 13,6%), dan Kriya (970 pelaku / 9,3%). "
            "Secara kumulatif, ketiganya menguasai 46,8% populasi pelaku usaha dan menyumbang lebih dari 74,2% terhadap total PDB "
            "ekonomi kreatif nasional (Kuliner Rp 668,1 T, Fesyen Rp 284,9 T, Kriya Rp 241,5 T). "
            "Namun, subsektor berbasis teknologi tinggi (Aplikasi, Game, dan DKV) mencatatkan laju pertumbuhan tahunan (YoY) tertinggi "
            "(mencapai 8,7% hingga 10,4%), membuktikan potensi nilai tambah tinggi yang siap menjadi lokomotif baru di masa depan."
        ),
        (
            "2. Disparitas Geografis (Jawa Sentris) dan Kesenjangan Indeks Digital Daerah",
            "Sebanyak 69,3% (7.257 pelaku) terkonsentrasi di 6 provinsi Pulau Jawa, dipimpin oleh Jawa Barat (2.232 pelaku / 21,3%), "
            "Jawa Timur (1.380 / 13,2%), dan DKI Jakarta (1.183 / 11,3%). Di luar Jawa, provinsi dengan pelaku tertinggi adalah "
            "Bali (485) dan Sumatera Utara (412). Kesenjangan ini berkorelasi kuat dengan Indeks Daya Saing Digital (EV-DCI Katadata): "
            "Provinsi di Jawa memiliki skor rata-rata 70–85, sedangkan daerah di Nusa Tenggara, Maluku, dan Papua berada di rentang 48–56. "
            "Disparitas logistik dan konektivitas internet menjadi bottleneck utama pemerataan ekonomi kreatif."
        ),
        (
            "3. Kausalitas Kuat Transformasi Digital terhadap Pertumbuhan Omzet Usaha",
            "Analisis komparatif membuktikan kausalitas nyata antara kedalaman digitalisasi dengan performa finansial UMKM: "
            "Sebanyak 80,2% pelaku berkategori 'Full Digital' (mengintegrasikan e-commerce/marketplace dan sistem kasir cloud POS) "
            "mencatatkan lonjakan pendapatan (42% di antaranya mengalami kenaikan omzet di atas 30%). Sebaliknya, pada pelaku UMKM "
            "offline/konvensional, mayoritas mengalami stagnasi omzet (52%) dan bahkan 23% mengalami penurunan pendapatan."
        ),
        (
            "4. Paradoks Akses Permodalan: Ketergantungan Modal Pribadi vs Potensi Fintech",
            "Meskipun pembiayaan merupakan pendorong utama ekspansi usaha (sebagaimana terbukti pada studi Amartha di mana 76,96% "
            "mitra pembiayaan mengalami kenaikan pendapatan dan 50.000 UMKM binaan berhasil naik kelas), sebanyak 58% pelaku ekraf "
            "masih bergantung pada modal sendiri/tabungan keluarga. Penetrasi Kredit Usaha Rakyat (KUR) perbankan baru mencapai 22%, "
            "dan Fintech P2P Lending produktif berizin OJK berada pada angka 12%. Hambatan terbesarnya adalah ketiadaan agunan fisik "
            "dan ketiadaan rekam jejak pembukuan keuangan standar."
        ),
        (
            "5. Kapasitas Penyerapan Tenaga Kerja dan Ketahanan Ekonomi Akar Rumput",
            "Setiap unit usaha mikro-kecil ekonomi kreatif menyerap rata-rata 2 hingga 4 tenaga kerja lokal non-formal (rata-rata 3,2 pekerja/unit). "
            "Secara nasional, sektor UMKM dan ekonomi kreatif menyerap 125,2 juta jiwa (97% tenaga kerja nasional). Daya lentur dan fleksibilitas "
            "sektor ini terbukti menjadi katup pengaman sosial-ekonomi yang mencegah lonjakan angka pengangguran terbuka pasca-pandemi."
        )
    ]

    for title, desc in insights:
        add_h2(title)
        add_p(desc)

    # ==============================================================================
    # BAB 5: VISUALISASI DATA & ARSITEKTUR DASHBOARD (BOBOT 20%)
    # ==============================================================================
    add_h1("5. Visualisasi Data & Arsitektur Dashboard (Bobot 20%)")
    add_p(
        "Visualisasi dashboard dirancang mengikuti prinsip visual perception dan data storytelling modern: "
        "kontras tinggi, keterbacaan intuitif bagi masyarakat umum, serta integrasi filter interaktif. "
        "Dashboard diimplementasikan ke dalam format Power BI Desktop (.pbix / .pbip) serta Web Dashboard interaktif 3 tab:"
    )
    add_p("• Kartu Skor Utama (KPI Cards): Menampilkan 5 metrik vital (Total Pelaku 10.478, Pemilik Usaha 60.3%, Konsentrasi Jawa 69.3%, Full Digital 36.4%, dan Mitra Naik Omzet 76.9%).")
    add_p("• Donut Chart (Status Pelaku): Memvisualisasikan segmentasi pengguna Ekraf Hub secara proporsional.")
    add_p("• Clustered Bar Chart (Top Subsektor): Menampilkan peringkat 12 subsektor teratas dengan conditional color coding.")
    add_p("• Regional Breakdown Bar Chart: Menunjukkan perbandingan populasi pelaku di provinsi utama Jawa vs Luar Jawa.")
    add_p("• 100% Stacked Bar Chart: Menggambarkan distribusi dampak digitalisasi terhadap omzet (Naik >30%, Naik 10-30%, Tetap, Menurun).")

    # Embed High-Res Infographic Image into Word
    img_landscape = "D:/final-project-ekraf/output/infografis_ekraf_final_project.png"
    if os.path.exists(img_landscape):
        add_h3("Tampilan Dashboard Infografis Resolusi Tinggi (Model Ekraf Hub Landscape):")
        doc.add_picture(img_landscape, width=Inches(6.5))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(4)
        p_cap.paragraph_format.space_after = Pt(12)
        r_cap = p_cap.add_run("Gambar 1: Visualisasi Dashboard Ekosistem & Akselerasi Digital UMKM Ekraf Indonesia (Sumber: Output Analisis Proyek)")
        r_cap.font.name = "Arial"
        r_cap.font.size = Pt(8.5)
        r_cap.font.italic = True
        r_cap.font.color.rgb = COLOR_MUTED

    # ==============================================================================
    # BAB 6: REKOMENDASI AKSI STRATEGIS (ACTIONABLE POLICIES) (BOBOT 15%)
    # ==============================================================================
    add_h1("6. Rekomendasi Kebijakan & Rencana Implementasi (Bobot 15%)")
    add_p(
        "Berdasarkan 5 Key Insights berbasis data di atas, disusun 4 rekomendasi kebijakan strategis yang konkret, terukur, "
        "dan dapat diimplementasikan oleh pemerintah, asosiasi pelaku usaha, maupun platform teknologi:"
    )

    recs = [
        (
            "Rekomendasi 1: Program Desentralisasi Logistik & Sentra Fulfillment Bersama di Luar Jawa",
            "Mengingat 69,3% pelaku terpusat di Jawa dan tingginya biaya logistik antar-pulau, pemerintah bersama platform e-commerce "
            "perlu menginisiasi subsidi ongkos kirim berbasis wilayah dan membangun Sentra Logistik Kreatif Bersama (Shared Fulfillment Hub) "
            "di titik strategis Luar Jawa (Medan, Makassar, Balikpapan, dan Denpasar) untuk menurunkan freight barrier produk kriya daerah."
        ),
        (
            "Rekomendasi 2: Inovasi Alternative Credit Scoring Berbasis Data Transaksi Ekraf Hub",
            "Untuk menjembatani gap permodalan di mana 58% UMKM masih modal sendiri, Kementerian Ekonomi Kreatif perlu mengintegrasikan data "
            "rekam jejak profil Ekraf Hub dengan platform Fintech P2P Lending produktif berizin OJK dan perbankan penyalur KUR. "
            "Omzet digital dan kepatuhan transaksi e-commerce dapat dijadikan substitusi agunan konvensional bagi UMKM unbanked."
        ),
        (
            "Rekomendasi 3: Kurasi Ekspor dan Sertifikasi Keberlanjutan Produk Fesyen & Kriya",
            "Dengan kontribusi ekspor fesyen ($18,5 miliar USD) dan kriya ($10,8 miliar USD) yang masif, perlu dibentuk program kurasi ekspor "
            "terpadu, pendampingan sertifikasi bahan baku ramah lingkungan (eco-friendly / sustainable crafts), serta pameran virtual terintegrasi "
            "untuk membuka akses pasar global nontradisional (Timur Tengah dan Eropa Timur)."
        ),
        (
            "Rekomendasi 4: Inkubasi Akselerasi 'Naik Kelas' dari Media Sosial ke Full-Digital",
            "Sebanyak 45% UMKM saat ini masih berada pada tahap digitalisasi dasar (hanya menggunakan chat medsos). Program pendampingan intensif "
            "harus diarahkan agar mereka mengadopsi sistem pembukuan digital dan kasir POS berbasis cloud, mengingat data membuktikan bahwa adopsi "
            "penuh melipatgandakan peluang kenaikan omzet di atas 30%."
        )
    ]

    for r_title, r_desc in recs:
        add_h2(r_title)
        add_p(r_desc)

    # Roadmap Action Matrix Table
    add_h3("Matriks Rencana Aksi Strategis (Implementation Matrix):")
    action_table = doc.add_table(rows=5, cols=4)
    action_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    action_table.autofit = False
    action_table.columns[0].width = Inches(1.8)
    action_table.columns[1].width = Inches(1.6)
    action_table.columns[2].width = Inches(1.6)
    action_table.columns[3].width = Inches(1.5)

    act_headers = ["Pilar Program Aksi", "Stakeholder Penanggung Jawab", "Target Penerima Manfaat", "Indikator Keberhasilan (KPI)"]
    for j, h in enumerate(act_headers):
        cell = action_table.cell(0, j)
        set_cell_background(cell, HEX_NAVY)
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    matrix_data = [
        (
            "Subsidi Logistik & Shared Hub Luar Jawa",
            "Kemenparekraf, Kemendag, Asosiasi E-Commerce (idEA)",
            "UMKM Kriya & Kuliner Kemasan Luar Pulau Jawa",
            "Penurunan biaya logistik 25%; volume kiriman naik 40%."
        ),
        (
            "Alternative Credit Scoring Fintech",
            "OJK, KemenkopUKM, Fintech Lending P2P, Bank Himbara",
            "50.000 UMKM Kreatif kategori Unbanked",
            "Penyaluran pembiayaan produktif Rp 2,5 Triliun; NPL < 2%."
        ),
        (
            "Kurasi & Akselerasi Ekspor Fesyen/Kriya",
            "Kemenparekraf, Kemenlu, Indonesian Trade Promotion Center",
            "Pelaku Fesyen Muslim & Kerajinan Ramah Lingkungan",
            "Kenaikan nilai devisa ekspor ekraf 15% YoY."
        ),
        (
            "Inkubasi Full-Digital & Kasir Cloud POS",
            "Google Career Certificates, Dinas Koperasi Daerah, FinTech POS",
            "100.000 UMKM Mikro tahap Medsos Dasar",
            "80% peserta mencatatkan peningkatan omzet usaha."
        )
    ]

    for i, row in enumerate(matrix_data):
        row_idx = i + 1
        bg = HEX_LIGHT_BG if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row):
            c = action_table.cell(row_idx, j)
            set_cell_background(c, bg)
            set_cell_margins(c, top=80, bottom=80, left=100, right=100)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # ==============================================================================
    # BAB 7: KESIMPULAN & TAUTAN PENGUMPULAN PORTOFOLIO
    # ==============================================================================
    add_h1("7. Kesimpulan & Tautan Pengumpulan Portofolio")
    add_p(
        "Final Project Track Data Analytics ini berhasil membuktikan bahwa pemanfaatan data analitik mampu mengungkap "
        "pola tersembunyi dari ekosistem ekonomi kreatif Indonesia. Sektor UMKM bukan hanya sekadar penyangga ekonomi, "
        "melainkan mesin penggerak utama pertumbuhan nasional yang memiliki daya tahan tinggi. Akselerasi digital yang merata "
        "dan inklusi pembiayaan yang tepat sasaran akan menjadi kunci utama pemerataan ekonomi dari desa hingga kota."
    )

    add_p(
        "Berikut adalah tautan pengumpulan portofolio resmi beserta berkas pendukung yang telah dipublikasikan:",
        bold_prefix="Tautan Portofolio Final: "
    )

    port_table = doc.add_table(rows=4, cols=2)
    port_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    port_table.autofit = False
    port_table.columns[0].width = Inches(2.2)
    port_table.columns[1].width = Inches(4.3)

    final_links = [
        ("Tautan Formulir Pengumpulan", "https://ekr.af/finalprojectda"),
        ("Tautan Dashboard Interaktif Web", "https://winxytri.github.io/final-project-ekraf/"),
        ("Tautan Repositori Kode & Data", "https://github.com/winxytri/final-project-ekraf"),
        ("Master File Excel Lokal", "D:\\final-project-ekraf\\data\\final_project_ekraf_master_data.xlsx")
    ]

    for i, (k, v) in enumerate(final_links):
        c0 = port_table.cell(i, 0)
        c1 = port_table.cell(i, 1)
        set_cell_background(c0, HEX_LIGHT_BG)
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, top=80, bottom=80, left=120, right=120)
        set_cell_margins(c1, top=80, bottom=80, left=120, right=120)

        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.font.name = "Arial"
        r0.font.size = Pt(9.5)
        r0.font.bold = True
        r0.font.color.rgb = COLOR_NAVY

        p1 = c1.paragraphs[0]
        if v.startswith("http"):
            add_hyperlink(p1, v, v, color="004B91")
        else:
            r1 = p1.add_run(v)
            r1.font.name = "Arial"
            r1.font.size = Pt(9.5)
            r1.font.color.rgb = COLOR_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(16)

    # Sign-off block
    p_sign = doc.add_paragraph()
    p_sign.paragraph_format.space_after = Pt(2)
    r_sign = p_sign.add_run("Disusun dan diajukan untuk memenuhi persyaratan kelulusan:\n")
    r_sign.font.name = "Arial"
    r_sign.font.size = Pt(9.5)
    r_sign.font.italic = True
    r_sign.font.color.rgb = COLOR_MUTED

    r_auth = p_sign.add_run("Peserta Google Career Certificates – Track Data Analytics\nProgram Creative Technology Future Talents Courses (Kemenparekraf RI 2026)")
    r_auth.font.name = "Arial"
    r_auth.font.size = Pt(10)
    r_auth.font.bold = True
    r_auth.font.color.rgb = COLOR_NAVY

    # Save document
    out_docx = "D:/final-project-ekraf/LAPORAN_FINAL_PROJECT_EKRAF.docx"
    doc.save(out_docx)
    print(f"Laporan Word (.docx) berhasil dibuat di: {out_docx}")

if __name__ == "__main__":
    create_report()
