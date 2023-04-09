import os 
import numpy as np 
import PIL as Image 
import keras_ocr
import cv2
import matplotlib.pyplot as plt
from file_manage import deleteImages

images_folder = "images"
def decode_predictions(scores, geometry):
	# grab the number of rows and columns from the scores volume, then
	# initialize our set of bounding box rectangles and corresponding
	# confidence scores
	(numRows, numCols) = scores.shape[2:4]
	rects = []
	confidences = []
	# loop over the number of rows
	for y in range(0, numRows):
		# extract the scores (probabilities), followed by the
		# geometrical data used to derive potential bounding box
		# coordinates that surround text
		scoresData = scores[0, 0, y]
		xData0 = geometry[0, 0, y]
		xData1 = geometry[0, 1, y]
		xData2 = geometry[0, 2, y]
		xData3 = geometry[0, 3, y]
		anglesData = geometry[0, 4, y]
		# loop over the number of columns
		for x in range(0, numCols):
			# if our score does not have sufficient probability,
			# ignore it
			if scoresData[x] < args["min_confidence"]:
				continue
			# compute the offset factor as our resulting feature
			# maps will be 4x smaller than the input image
			(offsetX, offsetY) = (x * 4.0, y * 4.0)
			# extract the rotation angle for the prediction and
			# then compute the sin and cosine
			angle = anglesData[x]
			cos = np.cos(angle)
			sin = np.sin(angle)
			# use the geometry volume to derive the width and height
			# of the bounding box
			h = xData0[x] + xData2[x]
			w = xData1[x] + xData3[x]
			# compute both the starting and ending (x, y)-coordinates
			# for the text prediction bounding box
			endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
			endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
			startX = int(endX - w)
			startY = int(endY - h)
			# add the bounding box coordinates and probability score
			# to our respective lists
			rects.append((startX, startY, endX, endY))
			confidences.append(scoresData[x])
	# return a tuple of the bounding boxes and associated confidences
	return (rects, confidences)

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
