import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from config import REPORT_PATH, CHART_PATH, REPORT_TITLE
from logger import get_logger

logger = get_logger()

def create_report(summary):
    try:
        print("Creating report directory...")

       
        os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

        print("Generating PDF...")
        doc = SimpleDocTemplate(REPORT_PATH)
        styles = getSampleStyleSheet()

        elements = []
        elements.append(Paragraph(REPORT_TITLE, styles["Title"]))

        for product, sales in summary.items():
            elements.append(Paragraph(f"{product}: ₹{sales}", styles["Normal"]))

        print("Adding chart...")
        elements.append(Image(CHART_PATH))

        doc.build(elements)

        logger.info("Report generated successfully")
        print(" Report created!")

    except Exception as e:
        logger.error(f"Error generating report: {e}")
        print("ERROR:", e)
        raise