#include <DigiMouse.h> 

void setup() {
  DigiMouse.begin();  
}

void moveTopLeft(){
    DigiMouse.move(100,-100,0);
    delay(500);
    DigiMouse.leftClick();
    delay(500);
//    while(true);/
  }

void loop() {
  DigiMouse.update();
//  for(int i = 0; i < 6; i++){///
//    DigiMouse.update();/
    int randomX = 100; // Move randomly along X-axis
    int randomY = -100;  // Move randomly along Y-axis
  
//  DigiMouse.moveX(randomX);
//  DigiMouse.leftClick();
//  delay(random(150, 500));
//  DigiMouse.moveY(randomY);
//    DigiMouse.move(randomX,randomY,0);
//    DigiMouse.move(randomX,randomY,0);
//    DigiMouse.move(randomX,randomY,0);
//    DigiMouse.move(randomX,randomY,0);
//    DigiMouse.move(randomX,randomY,0);
//    DigiMouse.move(randomX,randomY,0);
    moveTopLeft();

    delay(150);  // Random delay between movements
//  }  ///
//    DigiMouse.leftClick();///
    delay(150);
//    DigiMouse.rightClick();/
    delay(150);
//    while(true){/
//      /DigiMouse.update(); /
//    }///
}
