from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from joystick import Joystick


class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.mainUI()
        # self.showFullScreen()
        self.setWindowTitle("Kransteuerung")

    def mainUI(self):

        # electric magnet
        self.label_electric_magnet = QLabel(self)
        self.label_electric_magnet.setText("Elektromagnet")

        self.toggle_electric_magnet = QPushButton(self)
        self.toggle_electric_magnet.setCheckable(True)
        self.toggle_electric_magnet.setText("On/Off")

        # Create joystick
        self.joystick_left = Joystick()
        self.joystick_right = Joystick()

        # slider for servo
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setValue(50)

        self.slider_text = QLabel(self)
        self.slider_text.setText("Servomotor")
        

        # layout
        self.hbox_top = QHBoxLayout()
        self.hbox_top.addStretch()
        self.hbox_top.addWidget(self.label_electric_magnet) 
        self.hbox_top.addWidget(self.toggle_electric_magnet)
        self.hbox_top.addStretch()

        self.hbox_top2 = QHBoxLayout()
        self.hbox_top2.addStretch()
        self.hbox_top2.addWidget(self.slider_text)
        self.hbox_top2.addStretch()

        self.hbox_mid = QHBoxLayout()
        self.hbox_mid.addWidget(self.joystick_left)
        self.hbox_mid.addStretch()
        self.hbox_mid.addWidget(self.slider)
        self.hbox_mid.addStretch()
        self.hbox_mid.addWidget(self.joystick_right)

        self.vbox_main = QVBoxLayout(self)
        self.vbox_main.addLayout(self.hbox_top)
        self.vbox_main.addStretch()
        self.vbox_main.addLayout(self.hbox_top2)
        self.vbox_main.addLayout(self.hbox_mid)
        self.vbox_main.addStretch()
