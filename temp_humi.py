import grovepi

temp_humi_sensor = 8

def getdata():
	return grovepi.dht(temp_humi_sensor, 0)


if __name__ == "__main__":
	print getdata()
