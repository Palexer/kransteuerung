from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.mainUI()
        self.setWindowTitle("Kransteuerung")
        self.showFullScreen()

    def mainUI(self):

        self.heading = QLabel("Kransteuerung", self)
        self.heading.setStyleSheet("font-weight: bold; text-align: center;")

        # electric magnet
        self.label_electric_magnet = QLabel(self)
        self.label_electric_magnet.setText("Elektromagnet")

        self.toggle_electric_magnet = QPushButton(self)
        self.toggle_electric_magnet.setCheckable(True)
        self.toggle_electric_magnet.setText("On/Off")

        # slider for dc motor
        self.slider_dc_motor = QSlider(Qt.Horizontal, self)

        # buttons + label for servo
        self.servo_label = QLabel("Servo", self)
        self.servo_plus = QPushButton("+", self)
        self.servo_minus = QPushButton("-", self)
        

        self.slider_text = QLabel(self)
        self.slider_text.setText("DC Motor ")

        self.quit_btn = QPushButton(self)
        self.quit_btn.setText("Beenden")
        self.quit_btn.clicked.connect(sys.exit)

        # layout
        self.hbox_top = QHBoxLayout()
        self.hbox_top.addWidget(self.label_electric_magnet)
        self.hbox_top.addStretch() 
        self.hbox_top.addWidget(self.toggle_electric_magnet)

        self.hbox_mid = QHBoxLayout()
        self.hbox_mid.addWidget(self.slider_text)
        self.hbox_mid.addStretch()
        self.hbox_mid.addWidget(self.slider_dc_motor)

        self.hbox_bottom = QHBoxLayout()
        self.hbox_bottom.addWidget(self.servo_label)
        self.hbox_bottom.addStretch()
        self.hbox_bottom.addWidget(self.servo_plus)
        self.hbox_bottom.addWidget(self.servo_minus)

        self.vbox_main = QVBoxLayout(self)
        self.vbox_main.addWidget(self.heading)
        self.vbox_main.addLayout(self.hbox_top)
        self.vbox_main.addLayout(self.hbox_mid)
        self.vbox_main.addLayout(self.hbox_bottom)
        self.vbox_main.addStretch()
        self.vbox_main.addWidget(self.quit_btn)
