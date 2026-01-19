import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------- Paths ----------------
BASE_DIR = r"path location"
CSV_FILE = os.path.join(BASE_DIR, "simulated_environment_data.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

# Create output directory if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------- Load dataset ----------------
data = pd.read_csv(CSV_FILE)

# Convert timestamp to datetime
data["Timestamp"] = pd.to_datetime(data["Timestamp"])

# ---------------- Thresholds ----------------
TEMP_WARNING = 36
TEMP_CRITICAL = 40
AQI_WARNING = 101
AQI_CRITICAL = 200

# ---------------- Temperature Plot ----------------
plt.figure()
plt.plot(data["Timestamp"], data["Temperature_C"])
plt.axhline(TEMP_WARNING, linestyle="--", label="Warning Threshold")
plt.axhline(TEMP_CRITICAL, linestyle="--", label="Critical Threshold")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature vs Time")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "temperature_plot.png"))
plt.close()

# ---------------- AQI Plot ----------------
plt.figure()
plt.plot(data["Timestamp"], data["AQI"])
plt.axhline(AQI_WARNING, linestyle="--", label="Warning Threshold")
plt.axhline(AQI_CRITICAL, linestyle="--", label="Critical Threshold")
plt.xlabel("Time")
plt.ylabel("AQI")
plt.title("Air Quality Index vs Time")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "aqi_plot.png"))
plt.close()

# ---------------- Status Detection ----------------
def get_status(temp, aqi):
    if temp > TEMP_CRITICAL or aqi > AQI_CRITICAL:
        return "CRITICAL"
    elif temp >= TEMP_WARNING or aqi >= AQI_WARNING:
        return "WARNING"
    else:
        return "NORMAL"

data["Status"] = data.apply(
    lambda row: get_status(row["Temperature_C"], row["AQI"]),
    axis=1
)

print("Latest Environment Status:", data.iloc[-1]["Status"])
