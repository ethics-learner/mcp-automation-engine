import json
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

LOG_FILE = "logs/audit.log"

def export_json(out="logs/audit.json"):
    records = []
    with open(LOG_FILE) as f:
        for line in f:
            records.append({"entry": line.strip()})

    with open(out, "w") as f:
        json.dump(records, f, indent=2)

def export_pdf(out="logs/audit.pdf"):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(out)
    content = []

    with open(LOG_FILE) as f:
        for line in f:
            content.append(Paragraph(line.strip(), styles["Normal"]))

    doc.build(content)

if __name__ == "__main__":
    export_json()
    export_pdf()
