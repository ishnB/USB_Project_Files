#include <DigiMouse.h>
void setup(){
pinMode(1, OUTPUT);
DigiMouse.begin();
// Turn on LED for 0.25 seconds
digitalWrite(1, HIGH);
DigiMouse.delay(250);
digitalWrite(1, LOW);
}
void loop() {
DigiMouse.scroll(5);
//DigiMouse.scroll(-5);
DigiMouse.delay(100);
}
