# 🔹 AI-Assisted Smart Environmental Monitoring System

## 🔹 Problem Statement

Environmental conditions such as temperature, humidity, and air quality play a crucial role in human health, industrial safety, and smart infrastructure management. Traditional monitoring systems rely on static threshold-based alerts, which often fail to predict hazardous conditions in advance.

This project aims to design an **AI-assisted environmental monitoring system** that not only observes environmental parameters but also predicts potential risks and automatically triggers control actions. The system is designed to be scalable for real-world deployment using embedded systems and IoT platforms.

## 🔹 Objectives

* Monitor environmental parameters using simulated sensor data
* Classify environmental conditions into **Normal**, **Warning**, and **Critical**
* Design a system architecture suitable for embedded and IoT integration
* Lay the foundation for AI-based prediction and automation

## 🔹 Selected Environmental Parameters (Simulated)

| Parameter | Description |
|-----------|-------------|
| **Temperature** | Ambient temperature monitoring |
| **Humidity** | Moisture level in the environment |
| **Air Quality Index (AQI)** | Indicator of air pollution level |

## 🔹 System Outputs

The system categorizes the environment into:

* 🟢 **Normal** – Safe operating conditions
* 🟡 **Warning** – Early indication of unsafe trends
* 🔴 **Critical** – Immediate action required

## 🔹 System Architecture Overview

The architecture follows a **Sense → Analyze → Decide → Act** model.

1. **Sensors (Simulated)** collect environmental data
2. **Data Processing Module** evaluates real-time values
3. **AI Logic** predicts future risk levels
4. **Control Logic** determines system response
5. **Output** actions such as alerts or actuator triggers

📌 Refer to the diagram below for detailed architecture.

## 🔹 System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    SENSOR LAYER (Simulated)                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Temperature  │  │   Humidity   │  │     AQI      │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
└─────────┼──────────────────┼──────────────────┼─────────────┘
          │                  │                  │
          └──────────────────┼──────────────────┘
                             ▼
          ┌─────────────────────────────────────┐
          │    DATA PROCESSING MODULE           │
          │  • Data Collection                  │
          │  • Validation & Normalization       │
          └─────────────────┬───────────────────┘
                            ▼
          ┌─────────────────────────────────────┐
          │         AI LOGIC ENGINE             │
          │  • Classification (Normal/Warning/  │
          │    Critical)                        │
          │  • Predictive Analytics             │
          └─────────────────┬───────────────────┘
                            ▼
          ┌─────────────────────────────────────┐
          │       CONTROL LOGIC MODULE          │
          │  • Decision Making                  │
          │  • Action Triggering                │
          └─────────────────┬───────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    OUTPUT LAYER                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Alerts     │  │  Actuators   │  │   Logging    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

## 🔹 Day-2: Sensor Data Simulation

To mimic real embedded sensors, a Python-based sensor simulation module was developed. The system generates realistic temperature, humidity, and air quality data at fixed intervals and logs them into a CSV file for further processing.

### Simulated Parameters

- Temperature (°C)
- Humidity (%)
- Air Quality Index (AQI)

### Output

- Live console sensor readings
- Logged dataset stored in CSV format

This module enables software testing before deploying the system on real hardware.

## 🔹 Day-3: Data Visualization & Threshold Detection

Sensor data logged from the simulation module is processed and visualized to analyze environmental trends. Threshold-based classification is applied to categorize system states as Normal, Warning, or Critical.

### Features

- Time-series visualization of temperature and AQI
- Threshold-based status detection
- Automated environment classification

The visual analysis helps validate system behavior before applying AI-based prediction and hardware automation.

## 🔹 Day-4: AI-Based Prediction & Risk Assessment

An AI-assisted prediction module analyzes recent sensor data trends to forecast potential environmental risks. Instead of reacting only to current sensor values, the system predicts unsafe conditions in advance and recommends preventive actions.

### AI Logic Used

- Sliding window analysis
- Trend-based prediction
- Pre-emptive alert generation

This approach enables intelligent decision-making suitable for embedded and IoT-based automation systems.

## 🔹 Day-5: Embedded Control Logic & Automation

AI-based predictions are mapped to embedded system control logic to enable automatic hardware actions such as cooling, ventilation, and alarm triggering.

The system is designed to be compatible with Arduino and ESP-based controllers, enabling seamless transition from software simulation to real-world deployment.

## 🔹 Day-6: System Flow & Decision Modeling

To ensure clarity and scalability, the complete system workflow and decision-making logic are represented using flowcharts and decision trees.

### System Flow

- Continuous sensor monitoring
- Real-time data analysis
- AI-based risk prediction
- Automated control actions
- Closed-loop operation

### Decision Tree

The decision tree visually represents how the system transitions between Normal, Warning, and Critical states based on sensor values and AI predictions.

These diagrams help validate system logic and support future hardware and cloud deployment.

## 🔹 Technologies Planned

* **Python** (Data simulation & AI logic)
* **Embedded System Logic** (Arduino / ESP-ready)
* **IoT-ready** data flow design
* Data visualization and logging

## 🔹 Future Scope

* Integration with real sensors (DHT11, MQ series)
* Cloud dashboard using IoT platforms
* AI-based anomaly detection
* Automated cooling and ventilation control

## 🔹 Day-7: Project Summary & Final Documentation

### Project Workflow

1. Sensor data acquisition (simulated)
2. Data logging and visualization
3. Threshold-based condition detection
4. AI-assisted trend prediction
5. Embedded control logic mapping
6. Automated system response

## 🔹 Features

* Real-time sensor data simulation
* Environmental data visualization
* Threshold-based status detection
* AI-assisted risk prediction
* Embedded system control mapping
* Automation-ready system design

## 🔹 Results & Outputs

The system successfully:

* Generated realistic environmental sensor data
* Identified unsafe conditions using threshold logic
* Predicted potential risks before critical states
* Generated automated control decisions
* Visualized trends using time-series graphs

### 📊 Sample Outputs

* Temperature vs Time plot
* AQI vs Time plot
* Console-based AI prediction alerts

## 🔹 Technologies Used

* **Python** (Data simulation & AI logic)
* **Embedded System Logic** (Arduino / ESP-ready)
* **IoT-ready** data flow design
* Data visualization and logging

## 🔹 Future Scope

* Integration with real sensors (DHT11, MQ series)
* Cloud dashboard using IoT platforms
* AI-based anomaly detection
* Automated cooling and ventilation control

## 🔹 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/environmental-monitoring-system.git

# Navigate to project directory
cd environmental-monitoring-system

# Install dependencies
pip install -r requirements.txt
```

## 🔹 Usage

```bash
# Run the simulation
python main.py
```

## 🔹 Author
Gopi Ragul R
Embedded Systems | IoT | AI-assisted Automation

## 🔹 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🔹 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔹 Contact

For questions or suggestions, please open an issue or contact the maintainers.
