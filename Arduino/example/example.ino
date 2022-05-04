void setup() {
  Serial.begin(115200);
}
double i = 0.0;
void loop() {
  // plot sin wave with amplitude 5 and freq 5hz with sin wave amplitude 2 and freq 2 hz with up to 5% error
  i=5.0*sin(double(millis())/(200.00)*2.0*3.1416)*(1+0.05*random(-1000,1000)/1000)+2.0*sin(double(millis())/(500.00)*2.0*3.1416)*(1+0.05*random(-1000,1000)/1000);
  Serial.print("#Voltage, ms:");
  Serial.print(millis());
  Serial.print(", V:");
  Serial.print(i,6);

//  // duplicate
  Serial.print("; #current_reading, ms:");
  Serial.print(millis());
  Serial.print(", mA:");
  // plot sin wive with amplitude 120 and freq 10 hz
  Serial.print(120*sin(millis()*2.0*3.1416/100));

  
  Serial.print("; #current_reading, ms:");
  Serial.print(millis());
  Serial.print(", mA:");
  // plot cos wive with amplitude 100 and freq 1 hz
  Serial.println(100*cos(millis()*2.0*3.1416/1000));

}
