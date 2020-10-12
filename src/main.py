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
        self.slider_dc_motor.valueChanged.connect(lambda _: self.dc_motor(self.slider_dc_motor.value())) 
    
    def servo(self, increment):
        servoPin = 17
        g.setmode(g.BCM)
        g.setup(servoPin, g.OUT)
                
        p = g.PWM(servoPin, 50)
        p.start(5)
    
        try:
            try:
                if increment == True:
                    self.position += 1
                    p.ChangeDutyCycle(self.position)
                    sleep(1)
                    p.ChangeDutyCycle(0)

                else:
                    self.position -= 1
                    p.ChangeDutyCycle(self.position)
                    sleep(1)
                    p.ChangeDutyCycle(0)

            except ValueError:
                pass
                    
        except KeyboardInterrupt:
            p.stop()
            g.cleanup()

    def dc_motor(self, value):
        try:
            g.setmode(g.BCM)
            
            ena = 25
            in1 = 24
            in2 = 23
            
            g.setwarnings(False)
            g.setup(in1, g.OUT)
            g.setup(in2, g.OUT)
            g.setup(ena, g.OUT)
            
            pwm = g.PWM(ena, 100)
            pwm.start(0)

            pwm.ChangeDutyCycle(float(value)) # rotation
                    
            g.output(in1, True)
            g.output(in2, False)

        except KeyboardInterrupt:
            pwm.stop()
            g.cleanup()
 
def main():
    import sys
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
