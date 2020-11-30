from ui import UI
from PyQt5.QtWidgets import QApplication
import RPi.GPIO as gpio
from time import sleep

class App(UI):
    def __init__(self):
        super().__init__()
        self.position = 0
        self.rotation_value = 0
        self.dc_setup = False
        self.magnetOn = True
        
        # setup for dc motor
        gpio.setmode(gpio.BCM)
        
        self.ena = 25
        self.in1 = 24
        self.in2 = 23

        gpio.setwarnings(False)
        gpio.setup(self.in1, gpio.OUT)
        gpio.setup(self.in2, gpio.OUT)
        gpio.setup(self.ena, gpio.OUT)
        
        self.pwm = gpio.PWM(self.ena, 100)
        self.pwm.start(0)
        
        gpio.output(self.in1, True)
        gpio.output(self.in2, False)
        
    
        # connect functions to widgets        
        self.servo_plus.clicked.connect(lambda _: self.servo(True))  
        self.servo_minus.clicked.connect(lambda _: self.servo(False)) 
        self.slider_dc_motor.valueChanged.connect(self.pwm_change) 
        self.toggle_electric_magnet.clicked.connect(self.magnet)
    
    def servo(self, increment):
        servoPin = 17
        gpio.setmode(gpio.BCM)
        gpio.setup(servoPin, gpio.OUT)
                
        p = gpio.PWM(servoPin, 50)
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
            gpio.cleanup()
            
            
    def pwm_change(self, value):
        self.pwm.ChangeDutyCycle(float(value))

    def magnet(self):
        if self.magnetOn:
            self.magnetOn = False
            gpio.setup(18, gpio.OUT)
            gpio.output(18, gpio.HIGH)
        else:
            self.magnetOn = True
            gpio.setup(18, gpio.OUT)
            gpio.output(18, gpio.LOW)
            
 
def main():
    import sys
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
