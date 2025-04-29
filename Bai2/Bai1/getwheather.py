import csv
from datetime import datetime

total_temp = 0
total_humidity = 0
total_wind = 0

with open("weather_data.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        time_str = row["time"]
        date_obj = datetime.strptime(time_str, "%Y-%m-%dT%H:%M")
        if date_obj.date() <= datetime(2025, 4, 29).date():  # điều chỉnh năm nếu cần
            total_temp += float(row["temperature_2m"])
            total_humidity += float(row["relative_humidity_2m"])
            total_wind += float(row["wind_speed_10m"])

print("Tổng temperature_2m đến hết 29-04:", total_temp)
print("Tổng relative_humidity_2m đến hết 29-04:", total_humidity)
print("Tổng wind_speed_10m đến hết 29-04:", total_wind)
