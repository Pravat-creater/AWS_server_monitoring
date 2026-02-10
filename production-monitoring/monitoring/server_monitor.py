import psutil
import time
import os
from datetime import datetime

CPU_LIMIT = 20

# Get current file directory (VERY IMPORTANT)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALERT_FILE = os.path.join(BASE_DIR, "incident.log")

while True:
    cpu = psutil.cpu_percent(interval=1)

    if cpu > CPU_LIMIT:
        with open(ALERT_FILE, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} | High CPU detected: {cpu}%\n")
        print("ALERT: High CPU")
    else:
        print("CPU OK:", cpu)

    time.sleep(5)