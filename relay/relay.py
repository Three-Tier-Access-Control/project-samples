import RPi.GPIO  as GPIO
import time 

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)


try:
    while True:
        GPIO.output(16, GPIO.HIGH)
        print("Relay On")
        time.sleep(1)
        GPIO.output(16, GPIO.LOW)
        print("Relay Off")
        time.sleep(1)
finally:
    GPIO.cleanup()
