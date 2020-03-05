#include <ArduinoJson.h>
#include <SoftwareSerial.h>

StaticJsonBuffer<500> jsonBuffer;
SoftwareSerial rpi(10, 11); // RX, TX
String json;

void setup() {
  Serial.begin(38400);
  rpi.begin(38400);
}
// {"c1":"5","c2":"5","c3":"5","c4":"5"}
void loop() {
  if (rpi.available()) {
    json = rpi.readStringUntil("#"); // Until CR
    json.replace("#", "");
    Serial.println(json);
    JsonObject& root = jsonBuffer.parseObject(json);

    if (!root.success()) Serial.println("parseObject() failed");
    else Serial.println("done");
    const char* c1 = root["c1"];
    const char* c2 = root["c2"];
    const char* c3 = root["c3"];
    const char* c4 = root["c4"];
    Serial.println("--------------------------------");
    Serial.print("Candidate1 :");
    Serial.println(c1);
    Serial.print("Candidate2 :");
    Serial.println(c2);
    Serial.print("Candidate3 :");
    Serial.println(c3);
    Serial.print("Candidate4 :");
    Serial.println(c4);
    Serial.println("--------------------------------");
    delay(50);
  }
  json = "";
  delay(50);
}
