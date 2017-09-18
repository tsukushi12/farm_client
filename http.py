# -*- coding: utf-8 -*-
from config import FarmConf
import requests

watering_uri = "http://" + FarmConf.serv_ip + ":4567/"
queue_url = watering_uri + "queue"
completion_url = watering_uri + "completion"

def queue():
	res = requests.get(queue_url)
	return res

def completion():
	res = requests.get(completion_url)
	return res

