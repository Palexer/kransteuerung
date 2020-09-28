from UI import UI
from PyQt5.QtWidgets import QApplication
import RPi.GPIO as io
from time import sleep


class App(UI):
    def __init__(self):
        super().__init__() 
        self.position = 0
        self.servo_plus.clicked.connect(lambda _: self.servo(True))  
        self.servo_minus.clicked.connect(lambda _: self.servo(False))  
    
    def servo(self, increment:bool):
        servoPin = 17
        io.setmode(io.BCM)
        io.setup(servoPin, io.OUT)
                
        io = io.PWM(servoPin, 50)
        io.start(5)
    
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

    def dc_motor():
        io.setmode(io.BCM)
        
        ena = 25
        in1 = 24
        in2 = 23
        
        io.setwarnings(False)
        io.setup(in1, io.OUT)
        io.setup(in2, io.OUT)
        io.setup(ena, io.OUT)
        
        pwm = io.PWM(ena, 100)
        pwm.start(0)      
        
        io.output(in1, True)
        io.output(in2, False)

    def pwm_change(value):
        pwm.ChangeDutyCycle(float(value))
             
def main():
    import sys
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
