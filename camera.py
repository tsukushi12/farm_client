import time
import picamera
import io
import numpy as np

def take_a_picture():
	with picamera.PiCamera() as camera:
		camera.resolution = (1024, 768)
		camera.start_preview()
		time.sleep(2)
		camera.capture('image.jpg')
		return open("image.jpg", "rb")





def take_a_binary():
	with picamera.PiCamera() as camera:
		camera.resolution = (1024, 768)
		camera.start_preview()
		time.sleep(2) 
		stream = io.BytesIO()
		camera.capture(stream, format='jpeg')
		data = np.fromstring(stream.getvalue(), dtype=np.uint8)
		return (data)


if __name__ == "__main__":
	img = take_a_picture()
	with open("image.jpg", "wb") as fout:
		fout.write(img)
