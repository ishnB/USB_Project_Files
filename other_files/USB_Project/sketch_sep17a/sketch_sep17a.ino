#include <DigiMouse.h> 

void setup() {
  DigiMouse.begin();  
}

void loop() {
  DigiMouse.update();  
  int randomX = random(-10, 10);  // Move randomly along X-axis
  int randomY = random(-10, 10);  // Move randomly along Y-axis
  
  DigiMouse.moveX(randomX);
  delay(random(150, 500));
  DigiMouse.leftClick();
  delay(random(150, 500));
  DigiMouse.moveY(randomY);

  delay(random(150, 500));  // Random delay between movements
}
