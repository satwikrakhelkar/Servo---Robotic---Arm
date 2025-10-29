# Robotic Arm Controller with PCA9685

This project controls a 4-joint robotic arm using an Arduino and a PCA9685 servo driver. A PyQt6 GUI allows real-time control of each joint via sliders.

## 🧩 Hardware Overview

- **Arduino UNO/Nano**
- **PCA9685 (I²C servo driver)**
- **Servos:**
  - Channel 0 → 20kg digital servo (base rotation)
  - Channel 1 → MG996R (shoulder)
  - Channel 2 → MG995 (elbow)
  - Channel 3 → MG996R (gripper or wrist)

## 🖥 Software Components

- `servo_controller.ino`: Arduino sketch for receiving serial commands and controlling servos
- `servo_gui.py`: PyQt6 GUI with sliders for each joint

## 🔌 Wiring Summary

- PCA9685 SDA/SCL → Arduino A4/A5
- PCA9685 VCC → Arduino 5V
- PCA9685 V+ → External 5–6 V power supply
- PCA9685 GND → Shared with Arduino and power supply

## 🚀 Getting Started

1. Upload `servo_controller.ino` to your Arduino
2. Run `servo_gui.py` on your PC
3. Connect servos to PCA9685 channels 0–3
4. Use the GUI sliders to control each joint

## 📦 Future Plans

- Keyframe animation
- Timeline playback
- Save/load motion sequences
- Inverse kinematics

## 📸 Preview

![Robotic Arm Wiring Diagram](docs/wiring_diagram.png)

## 📄 License

MIT License (optional)
