import RPi.GPIO as GPIO
import time

POMP_PIN = 5
#GPIO.cleanup()
#time.sleep(1)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(POMP_PIN,GPIO.OUT)
GPIO.output(POMP_PIN,GPIO.HIGH)

