https://wokwi.com/projects/479263057093989377

#define LDRPIN A0
#define LEDPIN 8

void setup() {
  Serial.begin(9600);
  pinMode(LEDPIN, OUTPUT);
}

void loop() {
  int lightValue = analogRead(LDRPIN);

  Serial.print("Light Sensor Reading: ");
  Serial.println(lightValue);

  // TASK 1: Change the threshold to 500
  if (lightValue > 600) {
    digitalWrite(LEDPIN, HIGH);
  } else {
    digitalWrite(LEDPIN, LOW);
  }

  delay(500);
}
