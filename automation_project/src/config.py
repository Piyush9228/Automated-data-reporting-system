import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATA_FILE = os.path.join(BASE_DIR, "data", "sales.xlsx")


CHART_PATH = os.path.join(BASE_DIR, "output", "charts", "sales_chart.png")
REPORT_PATH = os.path.join(BASE_DIR, "output", "report.pdf")


LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")


EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"   # ⚠️ Use Gmail App Password
EMAIL_RECEIVER = "receiver@gmail.com"


REPORT_TITLE = "Daily Sales Report"