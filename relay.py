import RPi.GPIO as GPIO
import time
POMP_PIN = 5

def off_relay():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(POMP_PIN,GPIO.OUT)
	GPIO.output(POMP_PIN, GPIO.LOW)

def on_relay():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(POMP_PIN,GPIO.OUT)
	GPIO.output(POMP_PIN, GPIO.HIGH)

def watering_2():
	on_relay()
	time.sleep(2)
	off_relay()


