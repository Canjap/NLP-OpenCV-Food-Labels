import os 
import numpy as np 
import PIL as Image 
import keras_ocr
import cv2
import matplotlib.pyplot as plt
from file_manage import deleteImages

images_folder = "images"

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW) #DeviceShow: adds a source device param that actuates the next two lines
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
def Video(camera):
	if not camera.isOpened():
		print('cannot open cam')
		exit()
	index = 0
	while True: 
		ret, frame = camera.read() # bool ret = is the frame available? T or F value; image array vector frame = accesses the next frame the camera captures, based on default fps 
	
		if not ret: 
			print("Can't receive frame (stream end?). Exiting ...")
			break 
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame', gray) #displays the frame. bc its a while loop, this is continuous --> a video
		img_name = str(index) + ".png"
		img_save_to_path = fr'C:\Users\sanja\OneDrive\Documents\GitHub\NLP-OpenCV-Food-Labels\images\{img_name}'
		if index % 200 == 0:
			print('getting this frame...' + img_save_to_path)
			cv2.imwrite(img_save_to_path, frame) #saves the frame to the specified file 
		index+= 1
		
		if cv2.waitKey(1) == ord('q'): #if q is pressed on keyboard, the window closes. .waitKey() returns 32 bit int, w/ last 8 being the key. When AND operator is done to it, the last byte is left (last 8 ints). if this byte's ASCII key == q, then exit 
			break
	camera.release()
	cv2.destroyAllWindows()
deleteImages()
Video(camera)
