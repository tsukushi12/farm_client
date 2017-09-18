import http
import relay
import time

while True:
	que = http.queue()
	if que.text == "on":
		relay.watering_2()
		http.completion()
	time.sleep(5)
		
