from UI import UI
from backend import servo
from PyQt5.QtWidgets import QApplication

class App(UI):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
