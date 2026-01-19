import random
import time
import csv
import os
from datetime import datetime

# Sensor ranges
TEMP_MIN, TEMP_MAX = 20, 45        # Celsius
HUM_MIN, HUM_MAX = 30, 90          # Percentage
AQI_MIN, AQI_MAX = 50, 300         # AQI scale

# Directory & file
BASE_DIR = r"location"
CSV_FILE = os.path.join(BASE_DIR, "simulated_environment_data.csv")

def generate_sensor_data():
    temperature = round(random.uniform(TEMP_MIN, TEMP_MAX), 2)
    humidity = round(random.uniform(HUM_MIN, HUM_MAX), 2)
    aqi = random.randint(AQI_MIN, AQI_MAX)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [timestamp, temperature, humidity, aqi]

def main():
    # ✅ Create directory if it doesn't exist
    os.makedirs(BASE_DIR, exist_ok=True)

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write header only if file is empty
        if file.tell() == 0:
            writer.writerow(["Timestamp", "Temperature_C", "Humidity_%", "AQI"])

        print("Sensor simulation started... Press CTRL+C to stop")

        try:
            while True:
                data = generate_sensor_data()
                writer.writerow(data)
                file.flush()

                print(f"Temp: {data[1]}°C | Humidity: {data[2]}% | AQI: {data[3]}")
                time.sleep(2)

        except KeyboardInterrupt:
            print("\nSimulation stopped.")

if __name__ == "__main__":
    main()
