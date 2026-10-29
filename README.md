# Grade9-Automatic-Night-Light
https://wokwi.com/projects/479181038763508737

const int LDR_PIN = A0;
const int LED_PIN = 8;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int lightLevel = analogRead(LDR_PIN);

  if (lightLevel > 600) {
    digitalWrite(LED_PIN, HIGH);
    Serial.println("LED: ON - Dark condition");
  } else {
    digitalWrite(LED_PIN, LOW);
    Serial.println("LED: OFF - Bright condition");
  }

  Serial.print("Analog Reading: ");
  Serial.println(lightLevel);

  delay(1000);
}
