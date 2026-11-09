import os
import json
import zipfile

def build_pbit():
    base_dir = "d:/final-project-ekraf"
    pbit_path = os.path.join(base_dir, "Ekraf_Dashboard.pbit")
    
    # 1. Read model.bim and report.json from PBIP
    bim_path = os.path.join(base_dir, "Ekraf_Dashboard.SemanticModel", "model.bim")
    with open(bim_path, "r", encoding="utf-8") as f:
        model_bim = json.load(f)
        
    rep_path = os.path.join(base_dir, "Ekraf_Dashboard.Report", "report.json")
    with open(rep_path, "r", encoding="utf-8") as f:
        report_layout = json.load(f)

    # 2. Prepare XML & Metadata
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

    version_str = "2.126.927.0\x00"
    settings_json = {"version": "1.0"}
    metadata_json = {"version": 1, "type": 1}
    diagram_json = {"version": "1.0.0", "diagrams": []}

    # 3. Create ZIP archive for .pbit
    with zipfile.ZipFile(pbit_path, "w", zipfile.ZIP_DEFLATED) as z:
        # [Content_Types].xml (UTF-8)
        z.writestr("[Content_Types].xml", content_types_xml.encode("utf-8"))
        
        # Version (UTF-16LE)
        z.writestr("Version", version_str.encode("utf-16le"))
        
        # Settings (UTF-16LE)
        z.writestr("Settings", json.dumps(settings_json).encode("utf-16le"))
        
        # Metadata (UTF-16LE)
        z.writestr("Metadata", json.dumps(metadata_json).encode("utf-16le"))
        
        # DiagramLayout (UTF-16LE)
        z.writestr("DiagramLayout", json.dumps(diagram_json).encode("utf-16le"))
        
        # DataModelSchema (UTF-16LE)
        z.writestr("DataModelSchema", json.dumps(model_bim, indent=2).encode("utf-16le"))
        
        # Report/Layout (UTF-16LE)
        z.writestr("Report/Layout", json.dumps(report_layout, indent=2).encode("utf-16le"))

    print(f"Power BI Template file successfully created at: {pbit_path}")

if __name__ == "__main__":
    build_pbit()
