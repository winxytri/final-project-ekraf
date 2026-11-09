import os
import json
import zipfile

def build_pbip():
    base_dir = "d:/final-project-ekraf"
    excel_path = "D:/final-project-ekraf/data/final_project_ekraf_master_data.xlsx"
    
    # 1. Root PBIP File
    pbip_content = {
        "version": "1.0",
        "artifacts": [
            {
                "report": {
                    "path": "Ekraf_Dashboard.Report"
                }
            }
        ],
        "settings": {
            "enableAutoRecovery": True
        }
    }
    
    pbip_file = os.path.join(base_dir, "Ekraf_Dashboard.pbip")
    with open(pbip_file, "w", encoding="utf-8") as f:
        json.dump(pbip_content, f, indent=2)
    print(f"Created {pbip_file}")

    # 2. SemanticModel Directory
    sem_dir = os.path.join(base_dir, "Ekraf_Dashboard.SemanticModel")
    os.makedirs(sem_dir, exist_ok=True)
    
    with open(os.path.join(sem_dir, "definition.pbism"), "w", encoding="utf-8") as f:
        json.dump({"version": "1.0"}, f, indent=2)
        
    # Model.bim (TMSL JSON)
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
                            "expression": "COUNTROWS(Data_Responden_Hub)"
                        },
                        {
                            "name": "Total_Pemilik_Usaha",
                            "expression": "CALCULATE(COUNTROWS(Data_Responden_Hub), Data_Responden_Hub[Status_Pengguna] = \"Pemilik Usaha\")"
                        },
                        {
                            "name": "Persen_Pemilik_Usaha",
                            "expression": "DIVIDE([Total_Pemilik_Usaha], [Total_Pengguna_Terdaftar], 0)",
                            "formatString": "0.0%"
                        },
                        {
                            "name": "Pelaku_Full_Digital",
                            "expression": "CALCULATE(COUNTROWS(Data_Responden_Hub), Data_Responden_Hub[Tingkat_Digitalisasi] = \"Full Digital (Marketplace & POS)\")"
                        },
                        {
                            "name": "Persen_Adopsi_Digital",
                            "expression": "DIVIDE([Pelaku_Full_Digital], [Total_Pengguna_Terdaftar], 0)",
                            "formatString": "0.0%"
                        },
                        {
                            "name": "Pelaku_Kenaikan_Pendapatan",
                            "expression": "CALCULATE(COUNTROWS(Data_Responden_Hub), Data_Responden_Hub[Dampak_Digital_Thdp_Omzet] IN {\"Meningkat >30%\", \"Meningkat 10-30%\"})"
                        },
                        {
                            "name": "Persen_Kenaikan_Pendapatan",
                            "expression": "DIVIDE([Pelaku_Kenaikan_Pendapatan], [Total_Pengguna_Terdaftar], 0)",
                            "formatString": "0.0%"
                        },
                        {
                            "name": "Pelaku_Wilayah_Jawa",
                            "expression": "CALCULATE(COUNTROWS(Data_Responden_Hub), Data_Responden_Hub[Wilayah_Pulau] = \"Jawa\")"
                        },
                        {
                            "name": "Persen_Konsentrasi_Jawa",
                            "expression": "DIVIDE([Pelaku_Wilayah_Jawa], [Total_Pengguna_Terdaftar], 0)",
                            "formatString": "0.0%"
                        },
                        {
                            "name": "Rata_Rata_Omzet_Bulanan_Juta",
                            "expression": "AVERAGE(Data_Responden_Hub[Omzet_Bulanan_Juta_IDR])",
                            "formatString": "#,##0.0"
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
    print(f"Created {bim_file}")

    # 3. Report Directory
    rep_dir = os.path.join(base_dir, "Ekraf_Dashboard.Report")
    os.makedirs(rep_dir, exist_ok=True)
    
    pbir_content = {
        "version": "1.0",
        "datasetReference": {
            "byPath": {
                "path": "../Ekraf_Dashboard.SemanticModel"
            },
            "byConnection": None
        }
    }
    with open(os.path.join(rep_dir, "definition.pbir"), "w", encoding="utf-8") as f:
        json.dump(pbir_content, f, indent=2)

    # Report Layout JSON (report.json)
    # Define Section with KPI Cards, Donut, Bar Chart, Slicers
    report_layout = {
        "id": 0,
        "resourcePackages": [],
        "sections": [
            {
                "id": 0,
                "name": "Section_Overview_Ekraf",
                "displayName": "Ekosistem Ekraf & Akselerasi Digital",
                "filters": "[]",
                "ordinal": 0,
                "width": 1280.0,
                "height": 720.0,
                "config": json.dumps({
                    "name": "Section_Overview_Ekraf",
                    "layouts": [{"id": 0, "position": {"x": 0, "y": 0, "width": 1280, "height": 720}}]
                }),
                "visualContainers": [
                    # Visual 1: Title Header Card / TextBox
                    {
                        "x": 20.0,
                        "y": 15.0,
                        "z": 1,
                        "width": 1240.0,
                        "height": 55.0,
                        "config": json.dumps({
                            "name": "HeaderTextBox",
                            "layouts": [{"id": 0, "position": {"x": 20, "y": 15, "width": 1240, "height": 55}}],
                            "singleVisual": {
                                "visualType": "textbox",
                                "objects": {
                                    "general": [
                                        {"properties": {
                                            "paragraphs": [
                                                {
                                                    "textRuns": [
                                                        {"value": "EKOSISTEM & AKSELERASI DIGITAL UMKM EKONOMI KREATIF INDONESIA  ", "textStyle": {"fontFamily": "Segoe UI Bold", "fontSize": "16pt", "color": "#00D8D6"}},
                                                        {"value": "| Google Career Certificates x Kemenparekraf RI", "textStyle": {"fontFamily": "Segoe UI", "fontSize": "11pt", "color": "#94A3B8"}}
                                                    ]
                                                }
                                            ]
                                        }}
                                    ]
                                }
                            }
                        })
                    },
                    # Visual 2: Card KPI Total Pelaku
                    {
                        "x": 20.0,
                        "y": 80.0,
                        "z": 2,
                        "width": 230.0,
                        "height": 100.0,
                        "config": json.dumps({
                            "name": "CardTotalPelaku",
                            "layouts": [{"id": 0, "position": {"x": 20, "y": 80, "width": 230, "height": 100}}],
                            "singleVisual": {
                                "visualType": "card",
                                "projections": {
                                    "Fields": [{"queryRef": "Data_Responden_Hub.Total_Pengguna_Terdaftar"}]
                                }
                            }
                        }),
                        "query": json.dumps({
                            "Commands": [{
                                "SemanticQueryDataShapeCommand": {
                                    "Query": {
                                        "Version": 2,
                                        "From": [{"Name": "d", "Entity": "Data_Responden_Hub", "Type": 0}],
                                        "Select": [{"Measure": {"Expression": {"SourceRef": {"Source": "d"}}, "Property": "Total_Pengguna_Terdaftar"}, "Name": "Data_Responden_Hub.Total_Pengguna_Terdaftar"}]
                                    },
                                    "Binding": {"Primary": {"Groupings": [{"Projections": [0]}]}}
                                }
                            }]
                        })
                    },
                    # Visual 3: Card KPI % Pemilik Usaha
                    {
                        "x": 270.0,
                        "y": 80.0,
                        "z": 3,
                        "width": 230.0,
                        "height": 100.0,
                        "config": json.dumps({
                            "name": "CardPemilikUsaha",
                            "layouts": [{"id": 0, "position": {"x": 270, "y": 80, "width": 230, "height": 100}}],
                            "singleVisual": {
                                "visualType": "card",
                                "projections": {
                                    "Fields": [{"queryRef": "Data_Responden_Hub.Persen_Pemilik_Usaha"}]
                                }
                            }
                        }),
                        "query": json.dumps({
                            "Commands": [{
                                "SemanticQueryDataShapeCommand": {
                                    "Query": {
                                        "Version": 2,
                                        "From": [{"Name": "d", "Entity": "Data_Responden_Hub", "Type": 0}],
                                        "Select": [{"Measure": {"Expression": {"SourceRef": {"Source": "d"}}, "Property": "Persen_Pemilik_Usaha"}, "Name": "Data_Responden_Hub.Persen_Pemilik_Usaha"}]
                                    },
                                    "Binding": {"Primary": {"Groupings": [{"Projections": [0]}]}}
                                }
                            }]
                        })
                    },
                    # Visual 4: Card KPI % Konsentrasi Jawa
                    {
                        "x": 520.0,
                        "y": 80.0,
                        "z": 4,
                        "width": 230.0,
                        "height": 100.0,
                        "config": json.dumps({
                            "name": "CardKonsentrasiJawa",
                            "layouts": [{"id": 0, "position": {"x": 520, "y": 80, "width": 230, "height": 100}}],
                            "singleVisual": {
                                "visualType": "card",
                                "projections": {
                                    "Fields": [{"queryRef": "Data_Responden_Hub.Persen_Konsentrasi_Jawa"}]
                                }
                            }
                        }),
                        "query": json.dumps({
                            "Commands": [{
                                "SemanticQueryDataShapeCommand": {
                                    "Query": {
                                        "Version": 2,
                                        "From": [{"Name": "d", "Entity": "Data_Responden_Hub", "Type": 0}],
                                        "Select": [{"Measure": {"Expression": {"SourceRef": {"Source": "d"}}, "Property": "Persen_Konsentrasi_Jawa"}, "Name": "Data_Responden_Hub.Persen_Konsentrasi_Jawa"}]
                                    },
                                    "Binding": {"Primary": {"Groupings": [{"Projections": [0]}]}}
                                }
                            }]
                        })
                    },
                    # Visual 5: Card KPI % Adopsi Digital
                    {
                        "x": 770.0,
                        "y": 80.0,
                        "z": 5,
                        "width": 230.0,
                        "height": 100.0,
                        "config": json.dumps({
                            "name": "CardAdopsiDigital",
                            "layouts": [{"id": 0, "position": {"x": 770, "y": 80, "width": 230, "height": 100}}],
                            "singleVisual": {
                                "visualType": "card",
                                "projections": {
                                    "Fields": [{"queryRef": "Data_Responden_Hub.Persen_Adopsi_Digital"}]
                                }
                            }
                        }),
                        "query": json.dumps({
                            "Commands": [{
                                "SemanticQueryDataShapeCommand": {
                                    "Query": {
                                        "Version": 2,
                                        "From": [{"Name": "d", "Entity": "Data_Responden_Hub", "Type": 0}],
                                        "Select": [{"Measure": {"Expression": {"SourceRef": {"Source": "d"}}, "Property": "Persen_Adopsi_Digital"}, "Name": "Data_Responden_Hub.Persen_Adopsi_Digital"}]
                                    },
                                    "Binding": {"Primary": {"Groupings": [{"Projections": [0]}]}}
                                }
                            }]
                        })
                    },
                    # Visual 6: Card KPI % Kenaikan Omzet
                    {
                        "x": 1020.0,
                        "y": 80.0,
                        "z": 6,
                        "width": 240.0,
                        "height": 100.0,
                        "config": json.dumps({
                            "name": "CardNaikOmzet",
                            "layouts": [{"id": 0, "position": {"x": 1020, "y": 80, "width": 240, "height": 100}}],
                            "singleVisual": {
                                "visualType": "card",
                                "projections": {
                                    "Fields": [{"queryRef": "Data_Responden_Hub.Persen_Kenaikan_Pendapatan"}]
                                }
                            }
                        }),
                        "query": json.dumps({
                            "Commands": [{
                                "SemanticQueryDataShapeCommand": {
                                    "Query": {
                                        "Version": 2,
                                        "From": [{"Name": "d", "Entity": "Data_Responden_Hub", "Type": 0}],
                                        "Select": [{"Measure": {"Expression": {"SourceRef": {"Source": "d"}}, "Property": "Persen_Kenaikan_Pendapatan"}, "Name": "Data_Responden_Hub.Persen_Kenaikan_Pendapatan"}]
                                    },
                                    "Binding": {"Primary": {"Groupings": [{"Projections": [0]}]}}
                                }
                            }]
                        })
                    },
                    # Visual 7: Donut Chart - Status Pengguna
                    {
                        "x": 20.0,
                        "y": 195.0,
                        "z": 7,
                        "width": 380.0,
                        "height": 490.0,
                        "config": json.dumps({
                            "name": "DonutStatusPengguna",
                            "layouts": [{"id": 0, "position": {"x": 20, "y": 195, "width": 380, "height": 490}}],
                            "singleVisual": {
                                "visualType": "donutChart",
                                "projections": {
                                    "Category": [{"queryRef": "Data_Responden_Hub.Status_Pengguna"}],
                                    "Y": [{"queryRef": "Data_Responden_Hub.Total_Pengguna_Terdaftar"}]
                                }
                            }
                        })
                    },
                    # Visual 8: Bar Chart - Top Subsektor Ekraf
                    {
                        "x": 420.0,
                        "y": 195.0,
                        "z": 8,
                        "width": 460.0,
                        "height": 490.0,
                        "config": json.dumps({
                            "name": "BarSubsektorEkraf",
                            "layouts": [{"id": 0, "position": {"x": 420, "y": 195, "width": 460, "height": 490}}],
                            "singleVisual": {
                                "visualType": "barChart",
                                "projections": {
                                    "Category": [{"queryRef": "Subsektor_Ekraf.Subsektor"}],
                                    "Y": [{"queryRef": "Data_Responden_Hub.Total_Pengguna_Terdaftar"}]
                                }
                            }
                        })
                    },
                    # Visual 9: Bar Chart - Sebaran Regional Provinsi
                    {
                        "x": 900.0,
                        "y": 195.0,
                        "z": 9,
                        "width": 360.0,
                        "height": 490.0,
                        "config": json.dumps({
                            "name": "BarProvinsiEkraf",
                            "layouts": [{"id": 0, "position": {"x": 900, "y": 195, "width": 360, "height": 490}}],
                            "singleVisual": {
                                "visualType": "barChart",
                                "projections": {
                                    "Category": [{"queryRef": "Provinsi_Ekraf.Provinsi"}],
                                    "Y": [{"queryRef": "Data_Responden_Hub.Total_Pengguna_Terdaftar"}]
                                }
                            }
                        })
                    }
                ]
            }
        ]
    }
    
    rep_layout_file = os.path.join(rep_dir, "report.json")
    with open(rep_layout_file, "w", encoding="utf-8") as f:
        json.dump(report_layout, f, indent=2)
    print(f"Created {rep_layout_file}")
    
    print("\nPower BI Project (.pbip) generated successfully!")

if __name__ == "__main__":
    build_pbip()
