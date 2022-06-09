import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

try:
    print("Cleaning...")
finally:
        GPIO.cleanup()