# 🦾 Robotic Arm Controller with Dual PCA9685 Boards

This project controls a 5-joint robotic arm using an Arduino and two PCA9685 servo drivers. A PyQt6 GUI allows real-time control of each joint via sliders. The setup includes 4 high-torque servos and 1 mini servo (SG90), each mapped to a dedicated channel.

---

## 🧩 Hardware Overview

- **Arduino UNO/Nano**
- **PCA9685 #1 (address 0x40)** — high-torque servos
- **PCA9685 #2 (address 0x41)** — SG90 mini servo
- **Servos:**
  - Channel 0 → 20kg digital servo (base rotation)
  - Channel 1 → MG996R (shoulder)
  - Channel 2 → MG995 (elbow)
  - Channel 3 → MG996R (gripper or wrist)
  - Channel 4 (on PCA #2) → SG90 mini servo (fine gripper or wrist tilt)

---

## 🔌 Wiring Summary

### ✅ Arduino to Both PCA Boards (Shared I²C Bus)
| Arduino Pin | PCA9685 #1 | PCA9685 #2 |
|-------------|------------|------------|
| A4 (SDA)    | SDA        | SDA        |
| A5 (SCL)    | SCL        | SCL        |
| 5V          | VCC        | VCC        |
| GND         | GND        | GND        |

### ✅ Power Supply
- **PCA #1 V+** → 5–6 V, ≥5 A (for MG-class servos)
- **PCA #2 V+** → 5 V, ≥1 A (for SG90)
- **GND shared across Arduino, PCA #1, PCA #2, and both power supplies**

---

## 🖥 Software Components

- `Arduino/servo_controller.ino` — Arduino sketch for serial-controlled PWM output
- `Python/servo_gui.py` — PyQt6 GUI with sliders for each joint

---

## 🚀 Getting Started

1. Upload `servo_controller.ino` to your Arduino
2. Connect servos to PCA boards as per channel map
3. Run `servo_gui.py` on your PC
4. Use sliders to control each joint in real time

---

## 📦 Features

- Real-time control of 5 servos via GUI
- Safe dual-board architecture with isolated power
- Serial communication between PC and Arduino
- Modular code for easy expansion

---

## 🛠 Future Plans

- Keyframe animation and timeline playback
- Save/load motion sequences
- Inverse kinematics for coordinated movement
- GUI enhancements with joint labels and presets

---

## 📄 License

MIT License 
