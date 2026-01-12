from datetime import date
import os

LOG_FILE = "python_log.txt"
TOTAL_DAYS = 100

def load_log():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        return f.readlines()

def save_entry(entry):
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")

logs = load_log()
today = str(date.today())

# Check if already logged today
for line in logs:
    if line.startswith(today):
        print("✅ Already coded today. Stay dangerous.")
        exit()

day_number = len(logs) + 1

if day_number > TOTAL_DAYS:
    print("🏆 100 DAYS COMPLETED. You’re not normal any
