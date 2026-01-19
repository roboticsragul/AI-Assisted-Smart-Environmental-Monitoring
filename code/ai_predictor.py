import pandas as pd
import os

BASE_DIR = r"D:\TRACKS Project\forpy\pythonProject1"
CSV_FILE = os.path.join(BASE_DIR, "simulated_environment_data.csv")

WINDOW_SIZE = 5
TEMP_CRITICAL = 40
AQI_CRITICAL = 200

data = pd.read_csv(CSV_FILE)

recent = data.tail(WINDOW_SIZE)

def trend_rising(values):
    return values[-1] > values[0]

temp_vals = recent["Temperature_C"].values
aqi_vals = recent["AQI"].values

print("---- AI Prediction Output ----")

if trend_rising(temp_vals) and temp_vals[-1] > TEMP_CRITICAL - 3:
    print("⚠️ Predicted Temperature Risk: Cooling action recommended")
else:
    print("✅ Temperature trend stable")

if trend_rising(aqi_vals) and aqi_vals[-1] > AQI_CRITICAL - 20:
    print("⚠️ Predicted AQI Risk: Ventilation required")
else:
    print("✅ Air quality trend stable")
