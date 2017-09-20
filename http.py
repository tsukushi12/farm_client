# -*- coding: utf-8 -*-
from config import FarmConf
import requests


def queue():
	res = requests.get(FarmConf.queue_url)
	return res

def completion():
	res = requests.get(FarmConf.completion_url)
	return res

def post_data(sensor, data):
	requests.put(
			FarmConf.m2x_addr + sensor + "/value",
			headers=FarmConf.m2x_headers,
			data=data
			)	


if __name__ == "__main__":
	post_data("light", {"value" : 40})
