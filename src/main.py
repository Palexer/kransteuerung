from UI import UI
from PyQt5.QtWidgets import QApplication
import RPi.GPIO as g
from time import sleep


class App(UI):
    def __init__(self):
        super().__init__() 
        self.position = 0
        self.servo_plus.clicked.connect(lambda _: self.servo(True))  
        self.servo_minus.clicked.connect(lambda _: self.servo(False))  
    
    def servo(self, increment:bool):
        servoPin = 17
        g.setmode(g.BCM)
        g.setup(servoPin, g.OUT)
                
        p = g.PWM(servoPin, 50)
        p.start(50)
    
        try:
            if increment == True and self.position < 100:
                self.position += 1
                p.ChangeDutyCycle(self.position)
                sleep(1)
                p.ChangeDutyCycle(0)

            elif increment == False and self.position > 0:
                self.position -= 1
                p.ChangeDutyCycle(self.position)
                sleep(1)
                p.ChangeDutyCycle(0)

            p.stop()
            g.cleanup()
                    
        except KeyboardInterrupt:
            p.stop()
            g.cleanup()
    
                
def main():
    import sys
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
