import http
import light
import temp_humi
import time

while True:
	res = http.post_data("light", {"value" : light.getdata()})

	t_h = temp_humi.getdata()
	http.post_data("temp", {"value": t_h[0]})
	http.post_data("humi", {"value": t_h[1]})
	
	print res
	time.sleep(100)
