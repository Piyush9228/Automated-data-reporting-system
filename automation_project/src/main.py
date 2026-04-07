print("MAIN FILE STARTED")

from data_processing import load_data, process_data
from visualization import create_bar_chart
from report_generator import create_report
# from email_sender import send_email
from config import DATA_FILE

def run_pipeline():
    print("Pipeline started")

    df = load_data(DATA_FILE)
    print("Data loaded")

    summary = process_data(df)
    print("Data processed")

    create_bar_chart(summary)
    print("Chart created")

    create_report(summary)
    print("Report generated")

    print(" Done!")

if __name__ == "__main__":
    run_pipeline()