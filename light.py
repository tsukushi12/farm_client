import grovepi
import time

light_sensor = 0
grovepi.pinMode(light_sensor, "INPUT")

def getdata():
	sensor_value = grovepi.analogRead(light_sensor)
	return sensor_value

if __name__ == "__main__":
	time.sleep(3)
	print(getdata())
