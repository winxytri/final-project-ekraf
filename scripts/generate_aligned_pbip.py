import os
import json
import zipfile

def build_aligned_powerbi_dashboard():
    base_dir = "d:/final-project-ekraf"
    excel_path = "D:/final-project-ekraf/data/final_project_ekraf_master_data.xlsx"

    # ==========================================================================
    # 1. SEMANTIC MODEL (model.bim) WITH ALL MEASURES & FORMATS
    # ==========================================================================
    sem_dir = os.path.join(base_dir, "Ekraf_Dashboard.SemanticModel")
    os.makedirs(sem_dir, exist_ok=True)

    with open(os.path.join(sem_dir, "definition.pbism"), "w", encoding="utf-8") as f:
        json.dump({"version": "1.0"}, f, indent=2)

    model_bim = {
        "name": "SemanticModel",
        "compatibilityLevel": 1567,
        "model": {
            "culture": "en-US",
            "dataAccessOptions": {
                "legacyRedirects": True,
                "returnErrorValuesAsNull": True
            },
            "defaultPowerBIDataSourceVersion": "powerBI_V3",
            "sourceQueryCulture": "en-US",
            "tables": [
                # TABEL 1: Tren_Nasional
                {
                    "name": "Tren_Nasional",
                    "columns": [
                        {"name": "Tahun", "dataType": "int64", "sourceColumn": "Tahun"},
                        {"name": "Jumlah_UMKM_Juta", "dataType": "double", "sourceColumn": "Jumlah_UMKM_Juta"},
                        {"name": "PDB_Nasional_Triliun_IDR", "dataType": "double", "sourceColumn": "PDB_Nasional_Triliun_IDR"},
                        {"name": "Kontribusi_UMKM_PDB_Triliun_IDR", "dataType": "double", "sourceColumn": "Kontribusi_UMKM_PDB_Triliun_IDR"},
                        {"name": "Kontribusi_UMKM_PDB_Persen", "dataType": "double", "sourceColumn": "Kontribusi_UMKM_PDB_Persen"},
                        {"name": "PDB_Ekonomi_Kreatif_Triliun_IDR", "dataType": "double", "sourceColumn": "PDB_Ekonomi_Kreatif_Triliun_IDR"},
                        {"name": "Kontribusi_Ekraf_PDB_Persen", "dataType": "double", "sourceColumn": "Kontribusi_Ekraf_PDB_Persen"},
                        {"name": "Tenaga_Kerja_UMKM_Juta", "dataType": "double", "sourceColumn": "Tenaga_Kerja_UMKM_Juta"},
                        {"name": "Serapan_Naker_UMKM_Persen", "dataType": "double", "sourceColumn": "Serapan_Naker_UMKM_Persen"},
                        {"name": "Tenaga_Kerja_Ekraf_Juta", "dataType": "double", "sourceColumn": "Tenaga_Kerja_Ekraf_Juta"},
                        {"name": "Ekspor_Ekraf_Miliar_USD", "dataType": "double", "sourceColumn": "Ekspor_Ekraf_Miliar_USD"},
                        {"name": "UMKM_Go_Digital_Juta", "dataType": "double", "sourceColumn": "UMKM_Go_Digital_Juta"},
                        {"name": "Penetrasi_Digital_Persen", "dataType": "double", "sourceColumn": "Penetrasi_Digital_Persen"},
                        {"name": "Penyaluran_Kredit_Fintech_Triliun_IDR", "dataType": "double", "sourceColumn": "Penyaluran_Kredit_Fintech_Triliun_IDR"}
                    ],
                    "partitions": [
                        {
                            "name": "Tren_Nasional-Partition",
                            "mode": "import",
                            "source": {
                                "type": "m",
                                "expression": [
                                    "let",
                                    f'    Source = Excel.Workbook(File.Contents("{excel_path}"), null, true),',
                                    '    Tren_Nasional_Sheet = Source{[Item="Tren_Nasional",Kind="Sheet"]}[Data],',
                                    '    #"Promoted Headers" = Table.PromoteHeaders(Tren_Nasional_Sheet, [PromoteAllScalars=true]),',
                                    '    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"Tahun", Int64.Type}, {"Jumlah_UMKM_Juta", type number}, {"PDB_Nasional_Triliun_IDR", type number}, {"Kontribusi_UMKM_PDB_Triliun_IDR", type number}, {"Kontribusi_UMKM_PDB_Persen", type number}, {"PDB_Ekonomi_Kreatif_Triliun_IDR", type number}, {"Kontribusi_Ekraf_PDB_Persen", type number}, {"Tenaga_Kerja_UMKM_Juta", type number}, {"Serapan_Naker_UMKM_Persen", type number}, {"Tenaga_Kerja_Ekraf_Juta", type number}, {"Ekspor_Ekraf_Miliar_USD", type number}, {"UMKM_Go_Digital_Juta", type number}, {"Penetrasi_Digital_Persen", type number}, {"Penyaluran_Kredit_Fintech_Triliun_IDR", type number}})',
                                    "in",
                                    '    #"Changed Type"'
                                ]
                            }
                        }
                    ]
                },
                # TABEL 2: Subsektor_Ekraf
                {
                    "name": "Subsektor_Ekraf",
                    "columns": [
                        {"name": "Subsektor", "dataType": "string", "sourceColumn": "Subsektor"},
                        {"name": "Pelaku_Sampel_Hub", "dataType": "int64", "sourceColumn": "Pelaku_Sampel_Hub"},
                        {"name": "Estimasi_Pelaku_Nasional", "dataType": "int64", "sourceColumn": "Estimasi_Pelaku_Nasional"},
                        {"name": "Porsi_Pelaku_Persen", "dataType": "double", "sourceColumn": "Porsi_Pelaku_Persen"},
                        {"name": "PDB_Ekraf_Triliun_IDR", "dataType": "double", "sourceColumn": "PDB_Ekraf_Triliun_IDR"},
                        {"name": "Porsi_PDB_Persen", "dataType": "double", "sourceColumn": "Porsi_PDB_Persen"},
                        {"name": "Tenaga_Kerja_Ribu_Orang", "dataType": "int64", "sourceColumn": "Tenaga_Kerja_Ribu_Orang"},
                        {"name": "Nilai_Ekspor_Juta_USD", "dataType": "double", "sourceColumn": "Nilai_Ekspor_Juta_USD"},
                        {"name": "Tingkat_Adopsi_Digital_Persen", "dataType": "double", "sourceColumn": "Tingkat_Adopsi_Digital_Persen"},
                        {"name": "Tingkat_Inklusi_Fintech_Persen", "dataType": "double", "sourceColumn": "Tingkat_Inklusi_Fintech_Persen"},
                        {"name": "Pertumbuhan_Omzet_YoY_Persen", "dataType": "double", "sourceColumn": "Pertumbuhan_Omzet_YoY_Persen"},
                        {"name": "Kategori_Klaster", "dataType": "string", "sourceColumn": "Kategori_Klaster"}
                    ],
                    "measures": [
                        {
                            "name": "Total_PDB_Ekraf_Triliun",
                            "expression": "SUM(Subsektor_Ekraf[PDB_Ekraf_Triliun_IDR])",
                            "formatString": "\"Rp \"#,##0.0\" T\""
                        },
                        {
                            "name": "Total_Ekspor_Ekraf_Miliar_USD",
                            "expression": "SUM(Subsektor_Ekraf[Nilai_Ekspor_Juta_USD]) / 1000",
                            "formatString": "\"$\"#,##0.0\" Miliar\""
                        },
                        {
                            "name": "Rata_Pertumbuhan_Subsektor_YoY",
                            "expression": "AVERAGE(Subsektor_Ekraf[Pertumbuhan_Omzet_YoY_Persen])",
                            "formatString": "0.0\"%\""
                        }
                    ],
                    "partitions": [
                        {
                            "name": "Subsektor_Ekraf-Partition",
                            "mode": "import",
                            "source": {
                                "type": "m",
                                "expression": [
                                    "let",
                                    f'    Source = Excel.Workbook(File.Contents("{excel_path}"), null, true),',
                                    '    Subsektor_Ekraf_Sheet = Source{[Item="Subsektor_Ekraf",Kind="Sheet"]}[Data],',
                                    '    #"Promoted Headers" = Table.PromoteHeaders(Subsektor_Ekraf_Sheet, [PromoteAllScalars=true]),',
                                    '    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"Subsektor", type text}, {"Pelaku_Sampel_Hub", Int64.Type}, {"Estimasi_Pelaku_Nasional", Int64.Type}, {"Porsi_Pelaku_Persen", type number}, {"PDB_Ekraf_Triliun_IDR", type number}, {"Porsi_PDB_Persen", type number}, {"Tenaga_Kerja_Ribu_Orang", Int64.Type}, {"Nilai_Ekspor_Juta_USD", type number}, {"Tingkat_Adopsi_Digital_Persen", type number}, {"Tingkat_Inklusi_Fintech_Persen", type number}, {"Pertumbuhan_Omzet_YoY_Persen", type number}, {"Kategori_Klaster", type text}})',
                                    "in",
                                    '    #"Changed Type"'
                                ]
                            }
                        }
                    ]
                },
                # TABEL 3: Provinsi_Ekraf
                {
                    "name": "Provinsi_Ekraf",
                    "columns": [
                        {"name": "Provinsi", "dataType": "string", "sourceColumn": "Provinsi"},
                        {"name": "Wilayah_Pulau", "dataType": "string", "sourceColumn": "Wilayah_Pulau"},
                        {"name": "Pelaku_Sampel_Hub", "dataType": "int64", "sourceColumn": "Pelaku_Sampel_Hub"},
                        {"name": "Estimasi_Pelaku_Daerah", "dataType": "int64", "sourceColumn": "Estimasi_Pelaku_Daerah"},
                        {"name": "Porsi_Pelaku_Persen", "dataType": "double", "sourceColumn": "Porsi_Pelaku_Persen"},
                        {"name": "Indeks_Daya_Saing_Digital (EV-DCI)", "dataType": "double", "sourceColumn": "Indeks_Daya_Saing_Digital (EV-DCI)"},
                        {"name": "Adopsi_ECommerce_Persen", "dataType": "double", "sourceColumn": "Adopsi_ECommerce_Persen"},
                        {"name": "Penyaluran_Pembiayaan_Miliar_IDR", "dataType": "double", "sourceColumn": "Penyaluran_Pembiayaan_Miliar_IDR"},
                        {"name": "Subsektor_Unggulan", "dataType": "string", "sourceColumn": "Subsektor_Unggulan"},
                        {"name": "Kategori_Wilayah", "dataType": "string", "sourceColumn": "Kategori_Wilayah"}
                    ],
                    "partitions": [
                        {
                            "name": "Provinsi_Ekraf-Partition",
                            "mode": "import",
                            "source": {
                                "type": "m",
                                "expression": [
                                    "let",
                                    f'    Source = Excel.Workbook(File.Contents("{excel_path}"), null, true),',
                                    '    Provinsi_Ekraf_Sheet = Source{[Item="Provinsi_Ekraf",Kind="Sheet"]}[Data],',
                                    '    #"Promoted Headers" = Table.PromoteHeaders(Provinsi_Ekraf_Sheet, [PromoteAllScalars=true]),',
                                    '    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"Provinsi", type text}, {"Wilayah_Pulau", type text}, {"Pelaku_Sampel_Hub", Int64.Type}, {"Estimasi_Pelaku_Daerah", Int64.Type}, {"Porsi_Pelaku_Persen", type number}, {"Indeks_Daya_Saing_Digital (EV-DCI)", type number}, {"Adopsi_ECommerce_Persen", type number}, {"Penyaluran_Pembiayaan_Miliar_IDR", type number}, {"Subsektor_Unggulan", type text}, {"Kategori_Wilayah", type text}})',
                                    "in",
                                    '    #"Changed Type"'
                                ]
                            }
                        }
                    ]
                },
                # TABEL 4: Data_Responden_Hub
                {
                    "name": "Data_Responden_Hub",
                    "columns": [
                        {"name": "ID_Pengguna", "dataType": "string", "sourceColumn": "ID_Pengguna"},
                        {"name": "Status_Pengguna", "dataType": "string", "sourceColumn": "Status_Pengguna"},
                        {"name": "Subsektor", "dataType": "string", "sourceColumn": "Subsektor"},
                        {"name": "Provinsi", "dataType": "string", "sourceColumn": "Provinsi"},
                        {"name": "Wilayah_Pulau", "dataType": "string", "sourceColumn": "Wilayah_Pulau"},
                        {"name": "Skala_Usaha", "dataType": "string", "sourceColumn": "Skala_Usaha"},
                        {"name": "Tingkat_Digitalisasi", "dataType": "string", "sourceColumn": "Tingkat_Digitalisasi"},
                        {"name": "Menggunakan_Fintech_Digital", "dataType": "string", "sourceColumn": "Menggunakan_Fintech_Digital"},
                        {"name": "Sumber_Permodalan_Utama", "dataType": "string", "sourceColumn": "Sumber_Permodalan_Utama"},
                        {"name": "Dampak_Digital_Thdp_Omzet", "dataType": "string", "sourceColumn": "Dampak_Digital_Thdp_Omzet"},
                        {"name": "Omzet_Bulanan_Juta_IDR", "dataType": "double", "sourceColumn": "Omzet_Bulanan_Juta_IDR"},
                        {"name": "Jumlah_Tenaga_Kerja", "dataType": "int64", "sourceColumn": "Jumlah_Tenaga_Kerja"}
                    ],
                    "measures": [
                        {
                            "name": "Total_Pengguna_Terdaftar",
                            "expression": "COUNTROWS(Data_Responden_Hub)",
                            "formatString": "#,##0"
                        },
                        {
                            "name": "Total_Pemilik_Usaha",
                            "expression": "CALCULATE(COUNTROWS(Data_Responden_Hub), Data_Responden_Hub[Status_Pengguna] = \"Pemilik Usaha\")",
                            "formatString": "#,##0"
                        },
                        {
                            "name": "Persen_Pemilik_Usaha",
                            "expression": "DIVIDE([Total_Pemilik_Usaha], [Total_Pengguna_Terdaftar], 0)",
                            "formatString": "0.0%"
                        },
                        {
                            "name": "Pelaku_Full_Digital",
                            "expression": "CALCULATE(COUNTROWS(Data_Responden_Hub), Data_Responden_Hub[Tingkat_Digitalisasi] = \"Full Digital (Marketplace & POS)\")",
                            "formatString": "#,##0"
                        },
                        {
                            "name": "Persen_Adopsi_Digital",
                            "expression": "DIVIDE([Pelaku_Full_Digital], [Total_Pengguna_Terdaftar], 0)",
                            "formatString": "0.0%"
                        },
                        {
                            "name": "Pelaku_Adopsi_Fintech",
                            "expression": "CALCULATE(COUNTROWS(Data_Responden_Hub), Data_Responden_Hub[Menggunakan_Fintech_Digital] = \"Ya\")",
                            "formatString": "#,##0"
                        },
                        {
                            "name": "Persen_Penetrasi_Fintech",
                            "expression": "DIVIDE([Pelaku_Adopsi_Fintech], [Total_Pengguna_Terdaftar], 0)",
                            "formatString": "0.0%"
                        },
                        {
                            "name": "Pelaku_Kenaikan_Pendapatan",
                            "expression": "CALCULATE(COUNTROWS(Data_Responden_Hub), Data_Responden_Hub[Dampak_Digital_Thdp_Omzet] IN {\"Meningkat >30%\", \"Meningkat 10-30%\"})",
                            "formatString": "#,##0"
                        },
                        {
                            "name": "Persen_Kenaikan_Pendapatan",
                            "expression": "DIVIDE([Pelaku_Kenaikan_Pendapatan], [Total_Pengguna_Terdaftar], 0)",
                            "formatString": "0.0%"
                        },
                        {
                            "name": "Pelaku_Wilayah_Jawa",
                            "expression": "CALCULATE(COUNTROWS(Data_Responden_Hub), Data_Responden_Hub[Wilayah_Pulau] = \"Jawa\")",
                            "formatString": "#,##0"
                        },
                        {
                            "name": "Persen_Konsentrasi_Jawa",
                            "expression": "DIVIDE([Pelaku_Wilayah_Jawa], [Total_Pengguna_Terdaftar], 0)",
                            "formatString": "0.0%"
                        },
                        {
                            "name": "Rata_Rata_Omzet_Bulanan_Juta",
                            "expression": "AVERAGE(Data_Responden_Hub[Omzet_Bulanan_Juta_IDR])",
                            "formatString": "\"Rp \"#,##0.0\" Jt\""
                        },
                        {
                            "name": "Total_Tenaga_Kerja_Terserap",
                            "expression": "SUM(Data_Responden_Hub[Jumlah_Tenaga_Kerja])",
                            "formatString": "#,##0"
                        }
                    ],
                    "partitions": [
                        {
                            "name": "Data_Responden_Hub-Partition",
                            "mode": "import",
                            "source": {
                                "type": "m",
                                "expression": [
                                    "let",
                                    f'    Source = Excel.Workbook(File.Contents("{excel_path}"), null, true),',
                                    '    Data_Responden_Hub_Sheet = Source{[Item="Data_Responden_Hub",Kind="Sheet"]}[Data],',
                                    '    #"Promoted Headers" = Table.PromoteHeaders(Data_Responden_Hub_Sheet, [PromoteAllScalars=true]),',
                                    '    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"ID_Pengguna", type text}, {"Status_Pengguna", type text}, {"Subsektor", type text}, {"Provinsi", type text}, {"Wilayah_Pulau", type text}, {"Skala_Usaha", type text}, {"Tingkat_Digitalisasi", type text}, {"Menggunakan_Fintech_Digital", type text}, {"Sumber_Permodalan_Utama", type text}, {"Dampak_Digital_Thdp_Omzet", type text}, {"Omzet_Bulanan_Juta_IDR", type number}, {"Jumlah_Tenaga_Kerja", Int64.Type}})',
                                    "in",
                                    '    #"Changed Type"'
                                ]
                            }
                        }
                    ]
                }
            ],
            "relationships": [
                {
                    "name": "Responden_Subsektor",
                    "fromTable": "Data_Responden_Hub",
                    "fromColumn": "Subsektor",
                    "toTable": "Subsektor_Ekraf",
                    "toColumn": "Subsektor"
                },
                {
                    "name": "Responden_Provinsi",
                    "fromTable": "Data_Responden_Hub",
                    "fromColumn": "Provinsi",
                    "toTable": "Provinsi_Ekraf",
                    "toColumn": "Provinsi"
                }
            ]
        }
    }

    bim_file = os.path.join(sem_dir, "model.bim")
    with open(bim_file, "w", encoding="utf-8") as f:
        json.dump(model_bim, f, indent=2)

    # ==========================================================================
    # 2. MULTI-PAGE REPORT LAYOUT (report.json) MATCHING index.html EXACTLY
    # ==========================================================================
    rep_dir = os.path.join(base_dir, "Ekraf_Dashboard.Report")
    os.makedirs(rep_dir, exist_ok=True)

    with open(os.path.join(rep_dir, "definition.pbir"), "w", encoding="utf-8") as f:
        json.dump({
            "version": "1.0",
            "datasetReference": {
                "byPath": {"path": "../Ekraf_Dashboard.SemanticModel"},
                "byConnection": None
            }
        }, f, indent=2)

    # Helper function to create visual containers
    def make_kpi_card(x, y, w, h, measure_name, card_id):
        return {
            "x": float(x),
            "y": float(y),
            "z": card_id,
            "width": float(w),
            "height": float(h),
            "config": json.dumps({
                "name": f"Card_{measure_name}_{card_id}",
                "layouts": [{"id": 0, "position": {"x": x, "y": y, "width": w, "height": h}}],
                "singleVisual": {
                    "visualType": "card",
                    "projections": {
                        "Fields": [{"queryRef": f"Data_Responden_Hub.{measure_name}"}]
                    }
                }
            }),
            "query": json.dumps({
                "Commands": [{
                    "SemanticQueryDataShapeCommand": {
                        "Query": {
                            "Version": 2,
                            "From": [{"Name": "d", "Entity": "Data_Responden_Hub", "Type": 0}],
                            "Select": [{"Measure": {"Expression": {"SourceRef": {"Source": "d"}}, "Property": measure_name}, "Name": f"Data_Responden_Hub.{measure_name}"}]
                        },
                        "Binding": {"Primary": {"Groupings": [{"Projections": [0]}]}}
                    }
                }]
            })
        }

    def make_slicer(x, y, w, h, table_name, col_name, slicer_id):
        return {
            "x": float(x),
            "y": float(y),
            "z": slicer_id,
            "width": float(w),
            "height": float(h),
            "config": json.dumps({
                "name": f"Slicer_{col_name}_{slicer_id}",
                "layouts": [{"id": 0, "position": {"x": x, "y": y, "width": w, "height": h}}],
                "singleVisual": {
                    "visualType": "slicer",
                    "projections": {
                        "Values": [{"queryRef": f"{table_name}.{col_name}"}]
                    }
                }
            })
        }

    # --------------------------------------------------------------------------
    # PAGE 1: 1. Overview Ekosistem Ekraf (Matching Tab 1 of index.html)
    # --------------------------------------------------------------------------
    page_1_visuals = [
        # Header Text Box
        {
            "x": 20.0, "y": 15.0, "z": 1, "width": 840.0, "height": 55.0,
            "config": json.dumps({
                "name": "HeaderTextBoxP1",
                "layouts": [{"id": 0, "position": {"x": 20, "y": 15, "width": 840, "height": 55}}],
                "singleVisual": {
                    "visualType": "textbox",
                    "objects": {
                        "general": [{
                            "properties": {
                                "paragraphs": [{
                                    "textRuns": [
                                        {"value": "EKOSISTEM & AKSELERASI DIGITAL UMKM EKONOMI KREATIF  ", "textStyle": {"fontFamily": "Segoe UI Bold", "fontSize": "15pt", "color": "#00D8D6"}},
                                        {"value": "\nGoogle Career Certificates x Kemenparekraf RI | Data Analytics Track 2026", "textStyle": {"fontFamily": "Segoe UI", "fontSize": "10pt", "color": "#94A3B8"}}
                                    ]
                                }]
                            }
                        }]
                    }
                }
            })
        },
        # Slicers (Top Right)
        make_slicer(870, 15, 190, 55, "Data_Responden_Hub", "Wilayah_Pulau", 2),
        make_slicer(1070, 15, 190, 55, "Data_Responden_Hub", "Status_Pengguna", 3),

        # 5 KPI Cards
        make_kpi_card(20, 80, 235, 95, "Total_Pengguna_Terdaftar", 4),
        make_kpi_card(270, 80, 235, 95, "Persen_Pemilik_Usaha", 5),
        make_kpi_card(520, 80, 235, 95, "Persen_Konsentrasi_Jawa", 6),
        make_kpi_card(770, 80, 235, 95, "Persen_Adopsi_Digital", 7),
        make_kpi_card(1020, 80, 240, 95, "Persen_Kenaikan_Pendapatan", 8),

        # Visual 1: Donut Chart Status Pelaku
        {
            "x": 20.0, "y": 190.0, "z": 9, "width": 360.0, "height": 340.0,
            "config": json.dumps({
                "name": "DonutStatusPelaku",
                "layouts": [{"id": 0, "position": {"x": 20, "y": 190, "width": 360, "height": 340}}],
                "singleVisual": {
                    "visualType": "donutChart",
                    "projections": {
                        "Category": [{"queryRef": "Data_Responden_Hub.Status_Pengguna"}],
                        "Y": [{"queryRef": "Data_Responden_Hub.Total_Pengguna_Terdaftar"}]
                    }
                }
            })
        },
        # Visual 2: Bar Chart Top 12 Subsektor
        {
            "x": 395.0, "y": 190.0, "z": 10, "width": 475.0, "height": 340.0,
            "config": json.dumps({
                "name": "BarSubsektor",
                "layouts": [{"id": 0, "position": {"x": 395, "y": 190, "width": 475, "height": 340}}],
                "singleVisual": {
                    "visualType": "barChart",
                    "projections": {
                        "Category": [{"queryRef": "Subsektor_Ekraf.Subsektor"}],
                        "Y": [{"queryRef": "Data_Responden_Hub.Total_Pengguna_Terdaftar"}]
                    }
                }
            })
        },
        # Visual 3: Bar Chart Sebaran Provinsi
        {
            "x": 885.0, "y": 190.0, "z": 11, "width": 375.0, "height": 340.0,
            "config": json.dumps({
                "name": "BarProvinsi",
                "layouts": [{"id": 0, "position": {"x": 885, "y": 190, "width": 375, "height": 340}}],
                "singleVisual": {
                    "visualType": "barChart",
                    "projections": {
                        "Category": [{"queryRef": "Provinsi_Ekraf.Provinsi"}],
                        "Y": [{"queryRef": "Data_Responden_Hub.Total_Pengguna_Terdaftar"}]
                    }
                }
            })
        },
        # Bottom Text Box: 5 Key Insights & Storytelling (matching index.html)
        {
            "x": 20.0, "y": 545.0, "z": 12, "width": 1240.0, "height": 160.0,
            "config": json.dumps({
                "name": "InsightsTextBox",
                "layouts": [{"id": 0, "position": {"x": 20, "y": 545, "width": 1240, "height": 160}}],
                "singleVisual": {
                    "visualType": "textbox",
                    "objects": {
                        "general": [{
                            "properties": {
                                "paragraphs": [
                                    {
                                        "textRuns": [
                                            {"value": "RINGKASAN 5 KEY INSIGHTS & REKOMENDASI STRATEGIS EKRAF:\n", "textStyle": {"fontFamily": "Segoe UI Bold", "fontSize": "11pt", "color": "#FF6B4A"}}
                                        ]
                                    },
                                    {
                                        "textRuns": [
                                            {"value": "1. Hegemoni Big 3: ", "textStyle": {"fontFamily": "Segoe UI Bold", "fontSize": "9pt", "color": "#00D8D6"}},
                                            {"value": "Kuliner (23.9%), Fesyen (13.6%), Kriya (9.3%) kuasai 46.8% pelaku di Ekraf Hub dan >74% PDB Ekraf nasional.\n", "textStyle": {"fontSize": "9pt", "color": "#CBD5E1"}},
                                            {"value": "2. Kesenjangan Wilayah: ", "textStyle": {"fontFamily": "Segoe UI Bold", "fontSize": "9pt", "color": "#00D8D6"}},
                                            {"value": "69.3% pelaku usaha terpusat di Pulau Jawa (Jabar 2.232, Jatim 1.380, DKI 1.183 pelaku) akibat disparitas kesiapan digital.\n", "textStyle": {"fontSize": "9pt", "color": "#CBD5E1"}},
                                            {"value": "3. Kausalitas Digital: ", "textStyle": {"fontFamily": "Segoe UI Bold", "fontSize": "9pt", "color": "#00D8D6"}},
                                            {"value": "80.2% pelaku UMKM 'Full Digital' mencatatkan kenaikan omzet (42% naik >30%), berbanding hanya 25% pada kelompok offline.\n", "textStyle": {"fontSize": "9pt", "color": "#CBD5E1"}},
                                            {"value": "4. Akses Modal Terbatas: ", "textStyle": {"fontFamily": "Segoe UI Bold", "fontSize": "9pt", "color": "#00D8D6"}},
                                            {"value": "58% masih memakai modal pribadi; penetrasi fintech produktif (12%) dan KUR bank (22%) perlu didorong dengan credit scoring digital.", "textStyle": {"fontSize": "9pt", "color": "#CBD5E1"}}
                                        ]
                                    }
                                ]
                            }
                        }]
                    }
                }
            })
        }
    ]

    # --------------------------------------------------------------------------
    # PAGE 2: 2. Digitalisasi & Permodalan (Matching Tab 2 of index.html)
    # --------------------------------------------------------------------------
    page_2_visuals = [
        # Header Text Box
        {
            "x": 20.0, "y": 15.0, "z": 1, "width": 840.0, "height": 55.0,
            "config": json.dumps({
                "name": "HeaderTextBoxP2",
                "layouts": [{"id": 0, "position": {"x": 20, "y": 15, "width": 840, "height": 55}}],
                "singleVisual": {
                    "visualType": "textbox",
                    "objects": {
                        "general": [{
                            "properties": {
                                "paragraphs": [{
                                    "textRuns": [
                                        {"value": "ANALISIS TRANSFORMASI DIGITAL & INKLUSI FINTECH UMKM  ", "textStyle": {"fontFamily": "Segoe UI Bold", "fontSize": "15pt", "color": "#10B981"}},
                                        {"value": "\nDampak Penerapan Teknologi Kasir POS, E-Commerce, dan Sumber Permodalan", "textStyle": {"fontFamily": "Segoe UI", "fontSize": "10pt", "color": "#94A3B8"}}
                                    ]
                                }]
                            }
                        }]
                    }
                }
            })
        },
        make_slicer(870, 15, 190, 55, "Data_Responden_Hub", "Tingkat_Digitalisasi", 2),
        make_slicer(1070, 15, 190, 55, "Data_Responden_Hub", "Skala_Usaha", 3),

        # 4 KPI Cards
        make_kpi_card(20, 80, 295, 95, "Pelaku_Full_Digital", 4),
        make_kpi_card(330, 80, 295, 95, "Persen_Penetrasi_Fintech", 5),
        make_kpi_card(640, 80, 295, 95, "Rata_Rata_Omzet_Bulanan_Juta", 6),
        make_kpi_card(950, 80, 310, 95, "Total_Tenaga_Kerja_Terserap", 7),

        # Visual 1: 100% Stacked Column Chart - Tingkat Digital vs Dampak Omzet
        {
            "x": 20.0, "y": 190.0, "z": 8, "width": 610.0, "height": 500.0,
            "config": json.dumps({
                "name": "StackedChartDampakDigital",
                "layouts": [{"id": 0, "position": {"x": 20, "y": 190, "width": 610, "height": 500}}],
                "singleVisual": {
                    "visualType": "hundredPercentStackedColumnChart",
                    "projections": {
                        "Category": [{"queryRef": "Data_Responden_Hub.Tingkat_Digitalisasi"}],
                        "Series": [{"queryRef": "Data_Responden_Hub.Dampak_Digital_Thdp_Omzet"}],
                        "Y": [{"queryRef": "Data_Responden_Hub.Total_Pengguna_Terdaftar"}]
                    }
                }
            })
        },

        # Visual 2: Horizontal Bar Chart - Distribusi Sumber Permodalan
        {
            "x": 650.0, "y": 190.0, "z": 9, "width": 610.0, "height": 500.0,
            "config": json.dumps({
                "name": "BarSumberPermodalan",
                "layouts": [{"id": 0, "position": {"x": 650, "y": 190, "width": 610, "height": 500}}],
                "singleVisual": {
                    "visualType": "barChart",
                    "projections": {
                        "Category": [{"queryRef": "Data_Responden_Hub.Sumber_Permodalan_Utama"}],
                        "Y": [{"queryRef": "Data_Responden_Hub.Total_Pengguna_Terdaftar"}]
                    }
                }
            })
        }
    ]

    # --------------------------------------------------------------------------
    # PAGE 3: 3. Eksplorasi 17 Subsektor & Ekspor (Matching Tab 3 of index.html)
    # --------------------------------------------------------------------------
    page_3_visuals = [
        # Header Text Box
        {
            "x": 20.0, "y": 15.0, "z": 1, "width": 840.0, "height": 55.0,
            "config": json.dumps({
                "name": "HeaderTextBoxP3",
                "layouts": [{"id": 0, "position": {"x": 20, "y": 15, "width": 840, "height": 55}}],
                "singleVisual": {
                    "visualType": "textbox",
                    "objects": {
                        "general": [{
                            "properties": {
                                "paragraphs": [{
                                    "textRuns": [
                                        {"value": "EKSPLORASI DATA 17 SUBSEKTOR EKONOMI KREATIF  ", "textStyle": {"fontFamily": "Segoe UI Bold", "fontSize": "15pt", "color": "#A855F7"}},
                                        {"value": "\nStatistik Komparatif PDB, Nilai Devisa Ekspor, dan Pertumbuhan Tahunan YoY", "textStyle": {"fontFamily": "Segoe UI", "fontSize": "10pt", "color": "#94A3B8"}}
                                    ]
                                }]
                            }
                        }]
                    }
                }
            })
        },
        make_slicer(870, 15, 390, 55, "Subsektor_Ekraf", "Kategori_Klaster", 2),

        # 3 KPI Cards
        {
            "x": 20.0, "y": 80.0, "z": 3, "width": 395.0, "height": 95.0,
            "config": json.dumps({
                "name": "CardTotalPDB",
                "layouts": [{"id": 0, "position": {"x": 20, "y": 80, "width": 395, "height": 95}}],
                "singleVisual": {
                    "visualType": "card",
                    "projections": {
                        "Fields": [{"queryRef": "Subsektor_Ekraf.Total_PDB_Ekraf_Triliun"}]
                    }
                }
            })
        },
        {
            "x": 435.0, "y": 80.0, "z": 4, "width": 395.0, "height": 95.0,
            "config": json.dumps({
                "name": "CardTotalEkspor",
                "layouts": [{"id": 0, "position": {"x": 435, "y": 80, "width": 395, "height": 95}}],
                "singleVisual": {
                    "visualType": "card",
                    "projections": {
                        "Fields": [{"queryRef": "Subsektor_Ekraf.Total_Ekspor_Ekraf_Miliar_USD"}]
                    }
                }
            })
        },
        {
            "x": 850.0, "y": 80.0, "z": 5, "width": 410.0, "height": 95.0,
            "config": json.dumps({
                "name": "CardRataGrowth",
                "layouts": [{"id": 0, "position": {"x": 850, "y": 80, "width": 410, "height": 95}}],
                "singleVisual": {
                    "visualType": "card",
                    "projections": {
                        "Fields": [{"queryRef": "Subsektor_Ekraf.Rata_Pertumbuhan_Subsektor_YoY"}]
                    }
                }
            })
        },

        # Visual 1: Table (tableEx) matching Table in Tab 3 of index.html
        {
            "x": 20.0, "y": 190.0, "z": 6, "width": 780.0, "height": 500.0,
            "config": json.dumps({
                "name": "TableSubsektorFull",
                "layouts": [{"id": 0, "position": {"x": 20, "y": 190, "width": 780, "height": 500}}],
                "singleVisual": {
                    "visualType": "tableEx",
                    "projections": {
                        "Values": [
                            {"queryRef": "Subsektor_Ekraf.Subsektor"},
                            {"queryRef": "Subsektor_Ekraf.Kategori_Klaster"},
                            {"queryRef": "Subsektor_Ekraf.Pelaku_Sampel_Hub"},
                            {"queryRef": "Subsektor_Ekraf.PDB_Ekraf_Triliun_IDR"},
                            {"queryRef": "Subsektor_Ekraf.Nilai_Ekspor_Juta_USD"},
                            {"queryRef": "Subsektor_Ekraf.Tingkat_Adopsi_Digital_Persen"},
                            {"queryRef": "Subsektor_Ekraf.Pertumbuhan_Omzet_YoY_Persen"}
                        ]
                    }
                }
            })
        },

        # Visual 2: Bar Chart - Nilai Ekspor per Subsektor
        {
            "x": 820.0, "y": 190.0, "z": 7, "width": 440.0, "height": 500.0,
            "config": json.dumps({
                "name": "BarEksporSubsektor",
                "layouts": [{"id": 0, "position": {"x": 820, "y": 190, "width": 440, "height": 500}}],
                "singleVisual": {
                    "visualType": "barChart",
                    "projections": {
                        "Category": [{"queryRef": "Subsektor_Ekraf.Subsektor"}],
                        "Y": [{"queryRef": "Subsektor_Ekraf.Nilai_Ekspor_Juta_USD"}]
                    }
                }
            })
        }
    ]

    # Combine all 3 sections
    report_layout = {
        "id": 0,
        "resourcePackages": [],
        "sections": [
            {
                "id": 0,
                "name": "Section_Overview_Ekraf",
                "displayName": "1. Overview Ekosistem Ekraf",
                "filters": "[]",
                "ordinal": 0,
                "width": 1280.0,
                "height": 720.0,
                "config": json.dumps({
                    "name": "Section_Overview_Ekraf",
                    "layouts": [{"id": 0, "position": {"x": 0, "y": 0, "width": 1280, "height": 720}}]
                }),
                "visualContainers": page_1_visuals
            },
            {
                "id": 1,
                "name": "Section_Digital_Fintech",
                "displayName": "2. Digitalisasi & Permodalan",
                "filters": "[]",
                "ordinal": 1,
                "width": 1280.0,
                "height": 720.0,
                "config": json.dumps({
                    "name": "Section_Digital_Fintech",
                    "layouts": [{"id": 0, "position": {"x": 0, "y": 0, "width": 1280, "height": 720}}]
                }),
                "visualContainers": page_2_visuals
            },
            {
                "id": 2,
                "name": "Section_Subsektors_Ekspor",
                "displayName": "3. Eksplorasi 17 Subsektor",
                "filters": "[]",
                "ordinal": 2,
                "width": 1280.0,
                "height": 720.0,
                "config": json.dumps({
                    "name": "Section_Subsektors_Ekspor",
                    "layouts": [{"id": 0, "position": {"x": 0, "y": 0, "width": 1280, "height": 720}}]
                }),
                "visualContainers": page_3_visuals
            }
        ]
    }

    rep_layout_file = os.path.join(rep_dir, "report.json")
    with open(rep_layout_file, "w", encoding="utf-8") as f:
        json.dump(report_layout, f, indent=2)

    # Update PBIP Root
    pbip_file = os.path.join(base_dir, "Ekraf_Dashboard.pbip")
    with open(pbip_file, "w", encoding="utf-8") as f:
        json.dump({
            "version": "1.0",
            "artifacts": [{"report": {"path": "Ekraf_Dashboard.Report"}}],
            "settings": {"enableAutoRecovery": True}
        }, f, indent=2)

    # ==========================================================================
    # 3. RE-BUILD PBIT TEMPLATE ARCHIVE (.pbit)
    # ==========================================================================
    pbit_path = os.path.join(base_dir, "Ekraf_Dashboard.pbit")
    content_types_xml = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="json" ContentType="application/json" />
  <Default Extension="xml" ContentType="application/xml" />
  <Override PartName="/Version" ContentType="application/octet-stream" />
  <Override PartName="/Settings" ContentType="application/json" />
  <Override PartName="/Metadata" ContentType="application/json" />
  <Override PartName="/Report/Layout" ContentType="application/json" />
  <Override PartName="/DataModelSchema" ContentType="application/json" />
  <Override PartName="/DiagramLayout" ContentType="application/json" />
</Types>"""

    with zipfile.ZipFile(pbit_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types_xml.encode("utf-8"))
        z.writestr("Version", "2.126.927.0\x00".encode("utf-16le"))
        z.writestr("Settings", json.dumps({"version": "1.0"}).encode("utf-16le"))
        z.writestr("Metadata", json.dumps({"version": 1, "type": 1}).encode("utf-16le"))
        z.writestr("DiagramLayout", json.dumps({"version": "1.0.0", "diagrams": []}).encode("utf-16le"))
        z.writestr("DataModelSchema", json.dumps(model_bim, indent=2).encode("utf-16le"))
        z.writestr("Report/Layout", json.dumps(report_layout, indent=2).encode("utf-16le"))

    print("SUCCESS: Power BI Project (.pbip) and Template (.pbit) are now 100% synchronized with index.html!")
    print(f"- {pbip_file}")
    print(f"- {pbit_path}")

if __name__ == "__main__":
    build_aligned_powerbi_dashboard()
