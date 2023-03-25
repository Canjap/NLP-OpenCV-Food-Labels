import cv2 # OpenCV library
from pytesseract import pytesseract #tesseract - a library that is able to read text from images

import cv2
img = cv2.imread(r'C:\Users\sanja\OneDrive\Documents\GitHub\NLP-OpenCV-Food-Labels\nlp_diagram.png')

img = cv2.resize(img, (600, 360))
print(pytesseract.image_to_string(img))
cv2.imshow('Result', img)
cv2.waitKey(0)
