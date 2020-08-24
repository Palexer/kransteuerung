import RPi.GPIO as GPIO
import time

def servo(degrees, wait_time):
    
    servoPIN = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(2.5) # Initialization
    added_degrees = (0, 2.5, 5, 7.5, 5, 2.5, 0, -2.5)
    
    try:

        while True:

            for num in added_degrees:
                p.ChangeDutyCycle(degrees+num) # degrees for rotations
                time.sleep(wait_time) # wait between rotations
            
        
    except KeyboardInterrupt:
      p.stop()
      GPIO.cleanup()
