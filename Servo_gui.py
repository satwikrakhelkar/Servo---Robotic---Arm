import sys
import time
import serial
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PyQt6.QtCore import Qt

arduino = serial.Serial('COM9', 115200, timeout=1)
time.sleep(2)

class FiveServoUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Single PCA9685 - 5 Servo Controller")
        self.setGeometry(200, 200, 400, 350)

        layout = QVBoxLayout()

        # 20KG Servo
        self.servo20_label = QLabel("20KG Servo (Slider 0–70 → 200–270°)")
        self.servo20_slider = QSlider(Qt.Orientation.Horizontal)
        self.servo20_slider.setRange(0, 70)
        self.servo20_slider.setValue(35)
        self.servo20_slider.valueChanged.connect(self.update_20kg)
        layout.addWidget(self.servo20_label)
        layout.addWidget(self.servo20_slider)

        # MG996R
        self.mg996r_label = QLabel("MG996R Servo (0–180°)")
        self.mg996r_slider = QSlider(Qt.Orientation.Horizontal)
        self.mg996r_slider.setRange(0, 180)
        self.mg996r_slider.setValue(90)
        self.mg996r_slider.valueChanged.connect(self.update_mg996r)
        layout.addWidget(self.mg996r_label)
        layout.addWidget(self.mg996r_slider)

        # MG995
        self.mg995_label = QLabel("MG995 Servo (0–180°)")
        self.mg995_slider = QSlider(Qt.Orientation.Horizontal)
        self.mg995_slider.setRange(0, 180)
        self.mg995_slider.setValue(90)
        self.mg995_slider.valueChanged.connect(self.update_mg995)
        layout.addWidget(self.mg995_label)
        layout.addWidget(self.mg995_slider)

        # MG996R (360°)
        self.mg996r360_label = QLabel("MG996R Servo (0–360°)")
        self.mg996r360_slider = QSlider(Qt.Orientation.Horizontal)
        self.mg996r360_slider.setRange(0, 360)
        self.mg996r360_slider.setValue(180)
        self.mg996r360_slider.valueChanged.connect(self.update_mg996r360)
        layout.addWidget(self.mg996r360_label)
        layout.addWidget(self.mg996r360_slider)

        # SG90 Mini Servo
        self.sg90_label = QLabel("SG90 Mini Servo (0–90°)")
        self.sg90_slider = QSlider(Qt.Orientation.Horizontal)
        self.sg90_slider.setRange(0, 90)
        self.sg90_slider.setValue(45)
        self.sg90_slider.valueChanged.connect(self.update_sg90)
        layout.addWidget(self.sg90_label)
        layout.addWidget(self.sg90_slider)

        self.setLayout(layout)

    def update_20kg(self):
        val = self.servo20_slider.value()
        angle = int(val * (270 - 200) / 70 + 200)
        self.servo20_label.setText(f"20KG Servo: {angle}°")
        arduino.write(f"M0{angle}\n".encode())

    def update_mg996r(self):
        angle = self.mg996r_slider.value()
        self.mg996r_label.setText(f"MG996R Servo: {angle}°")
        arduino.write(f"M1{angle}\n".encode())

    def update_mg995(self):
        angle = self.mg995_slider.value()
        self.mg995_label.setText(f"MG995 Servo: {angle}°")
        arduino.write(f"M2{angle}\n".encode())

    def update_mg996r360(self):
        angle = self.mg996r360_slider.value()
        self.mg996r360_label.setText(f"MG996R (360°): {angle}°")
        arduino.write(f"M3{angle}\n".encode())

    def update_sg90(self):
        angle = self.sg90_slider.value()
        self.sg90_label.setText(f"SG90 Mini Servo: {angle}°")
        arduino.write(f"M4{angle}\n".encode())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FiveServoUI()
    window.show()
    sys.exit(app.exec())
