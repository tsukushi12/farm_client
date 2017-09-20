class FarmConf():
	serv_ip = "192.168.0.8"
	watering_uri = "http://" + serv_ip + ":4567/"
	queue_url = watering_uri + "queue"
	completion_url = watering_uri + "completion"

	m2x_addr = "http://api-m2x.att.com/v2/devices/dfcdc0e18c63a51d926c173f4a3a9d2f/streams/"
	m2x_headers = {
		"X-M2X-KEY" : "f323f3b0cbc638dcc4405c7f941b1e50",
		 "Content-Type" : "application/json"
		}


