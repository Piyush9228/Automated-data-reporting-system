import os
import matplotlib.pyplot as plt
from config import CHART_PATH
from logger import get_logger

logger = get_logger()

def create_bar_chart(summary):
    try:
        folder = os.path.dirname(CHART_PATH)

       
        if os.path.exists(folder) and not os.path.isdir(folder):
            os.remove(folder)

        os.makedirs(folder, exist_ok=True)

        summary.plot(kind="bar")
        plt.title("Sales by Product")
        plt.savefig(CHART_PATH)
        plt.close()

        print("Chart created!")

    except Exception as e:
        print("ERROR:", e)
        raise