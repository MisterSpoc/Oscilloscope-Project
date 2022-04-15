#include <Arduino.h>

void setup() {
  Serial.begin(57600);
}

void loop() {
  Serial.print("1: ");
  Serial.print(5.0*rand());
  Serial.print(",");
  Serial.print("2: ");
  Serial.print(5.0*rand());
  Serial.println();
  
  delay(100);
}