import light
import temp_humi
import camera
import http
import config

def make_data():
	light_data = light.getdata()
	temp, humi = temp_humi.getdata()
	picture = camera.take_a_picture()
	data = {
		"key":config.key,
		"light":light_data,
		"temp":temp,
		"humi":humi,
		"soil_humi":10
	}
	file = {"files":picture}
	return [file, data]

def main():
	data = make_data()
	res = http.api_post(*data)
	return res


if __name__ == "__main__":
	print(main())
