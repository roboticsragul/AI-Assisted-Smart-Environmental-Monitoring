// Pseudo Arduino Control Logic

#define FAN_PIN 5
#define VENT_PIN 6
#define ALARM_PIN 7

float temperature;
int aqi;

bool temp_risk;
bool aqi_risk;

void setup() {
  pinMode(FAN_PIN, OUTPUT);
  pinMode(VENT_PIN, OUTPUT);
  pinMode(ALARM_PIN, OUTPUT);

  digitalWrite(FAN_PIN, LOW);
  digitalWrite(VENT_PIN, LOW);
  digitalWrite(ALARM_PIN, LOW);
}

void loop() {

  // Values received from AI module
  // temperature = ...
  // aqi = ...
  // temp_risk = ...
  // aqi_risk = ...

  if (temp_risk && temperature > 37) {
    digitalWrite(FAN_PIN, HIGH);
  } else {
    digitalWrite(FAN_PIN, LOW);
  }

  if (aqi_risk && aqi > 180) {
    digitalWrite(VENT_PIN, HIGH);
  } else {
    digitalWrite(VENT_PIN, LOW);
  }

  if (temperature > 40 || aqi > 220) {
    digitalWrite(ALARM_PIN, HIGH);
  } else {
    digitalWrite(ALARM_PIN, LOW);
  }

  delay(1000);
}
