#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40);

// Pulse ranges
const int SERVO_20KG_MIN = 500, SERVO_20KG_MAX = 2500;
const int MG996R_MIN = 500, MG996R_MAX = 2500;
const int MG995_MIN = 600, MG995_MAX = 2400;
const int SG90_MIN = 600, SG90_MAX = 2400;

uint16_t angleToTicks(int angle, int us_min, int us_max, int max_angle) {
  int us = map(angle, 0, max_angle, us_min, us_max);
  return (uint16_t)((us * 4096L) / 20000L);
}

void setup() {
  Serial.begin(115200);
  Wire.begin();
  pwm.begin();
  pwm.setPWMFreq(50);
  delay(100);
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    input.trim();

    if (input.startsWith("M0")) {
      int angle = input.substring(2).toInt();
      angle = constrain(angle, 200, 270);
      pwm.setPWM(0, 0, angleToTicks(angle, SERVO_20KG_MIN, SERVO_20KG_MAX, 270));
    } else if (input.startsWith("M1")) {
      int angle = input.substring(2).toInt();
      angle = constrain(angle, 0, 180);
      pwm.setPWM(1, 0, angleToTicks(angle, MG996R_MIN, MG996R_MAX, 180));
    } else if (input.startsWith("M2")) {
      int angle = input.substring(2).toInt();
      angle = constrain(angle, 0, 180);
      pwm.setPWM(2, 0, angleToTicks(angle, MG995_MIN, MG995_MAX, 180));
    } else if (input.startsWith("M3")) {
      int angle = input.substring(2).toInt();
      angle = constrain(angle, 0, 360);
      pwm.setPWM(3, 0, angleToTicks(angle, MG996R_MIN, MG996R_MAX, 360));
    } else if (input.startsWith("M4")) {
      int angle = input.substring(2).toInt();
      angle = constrain(angle, 0, 90);
      pwm.setPWM(4, 0, angleToTicks(angle, SG90_MIN, SG90_MAX, 90));
    }
  }
}
