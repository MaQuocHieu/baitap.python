import requests
import csv

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "past_days": 10,
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

response = requests.get(url, params=params)
data = response.json()

# Lưu dữ liệu vào file CSV
with open("weather_data.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["latitude", "longitude", "time", "temperature_2m", "relative_humidity_2m", "wind_speed_10m"])
    for i in range(len(data["hourly"]["time"])):
        writer.writerow([
            data["latitude"],
            data["longitude"],
            data["hourly"]["time"][i],
            data["hourly"]["temperature_2m"][i],
            data["hourly"]["relative_humidity_2m"][i],
            data["hourly"]["wind_speed_10m"][i]
        ])
