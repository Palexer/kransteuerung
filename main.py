from PyQt5.QtWidgets import *
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

        # layout
        self.hbox_top = QHBoxLayout()
        self.hbox_top.addWidget(self.label_electric_magnet) 
        self.hbox_top.addWidget(self.toggle_electric_magnet) 
        self.hbox_top.addStretch()

        self.hbox_mid = QHBoxLayout()
        self.hbox_mid.addWidget(self.joystick_left)
        self.hbox_mid.addStretch()
        self.hbox_mid.addWidget(self.joystick_right)

        self.vbox_main = QVBoxLayout(self)
        self.vbox_main.addLayout(self.hbox_top)
        self.vbox_main.addStretch()
        self.vbox_main.addLayout(self.hbox_mid)
        self.vbox_main.addStretch()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())
