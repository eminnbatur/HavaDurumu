import csv
from datetime import datetime

def save_weather_data(data, filename="gecmis_veriler.csv"):
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([
            now,
            data["city"],
            data["temperature"],
            data["description"],
            data["humidity"]
        ])
