import smtplib
from email.message import EmailMessage
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, REPORT_PATH
from logger import get_logger

logger = get_logger()

def send_email():
    try:
        msg = EmailMessage()
        msg["Subject"] = "Daily Sales Report"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        msg.set_content("Please find attached report.")

        with open(REPORT_PATH, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="pdf",
                filename="report.pdf"
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)

        logger.info("Email sent successfully")
    except Exception as e:
        logger.error(f"Error sending email: {e}")
        raise