# Automated Data Reporting System

## Overview

This project is an automated data reporting system built using Python. It reads data from Excel files, processes and analyzes it, generates visual insights, and creates PDF reports. The system can be scheduled to run automatically, making it suitable for real-world business reporting workflows.

## Features

* Reads and processes Excel data using Pandas
* Generates charts using Matplotlib
* Creates PDF reports using ReportLab
* Logs execution details for monitoring and debugging
* Supports automation via Task Scheduler

## Tech Stack

* Python
* Pandas
* Matplotlib
* OpenPyXL
* ReportLab

## Project Structure

```
automation_project/
│
├── data/
├── output/
├── logs/
├── src/
│   ├── config.py
│   ├── data_processing.py
│   ├── visualization.py
│   ├── report_generator.py
│   ├── email_sender.py
│   └── main.py
```

## Installation

```
git clone https://github.com/Piyush9228/Automated-data-reporting-system.git
cd Automated-data-reporting-system
pip install -r requirements.txt
```

## Usage

```
python src/main.py
```

## Output

* Chart: `output/charts/sales_chart.png`
* Report: `output/report.pdf`
* Logs: `logs/app.log`

## Automation

The project can be scheduled using Windows Task Scheduler to run automatically at a specified time, enabling hands-free reporting.

## Future Enhancements

* Add Streamlit dashboard
* Integrate email notifications
* Deploy using Docker
* Add cloud storage support

## Author

Piyush Kumar
