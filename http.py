import requests
import config
import json

def api_post( files, data ):
	res = requests.post(config.post_url, data=data, files=files)
	return res.json()[0]

def api_get():
	res = requests.get(config.get_url)
	return res.json()[0]


if __name__ == "__main__":
	res = api_get()
	print(res)
