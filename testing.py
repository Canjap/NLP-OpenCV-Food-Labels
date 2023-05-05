import cv2 # OpenCV library
from pytesseract import pytesseract #tesseract - a library that is able to read text from images
from PIL import Image #a Python image processing lib

camera = cv2.VideoCapture(0)

while True: 
    _, Image=camera.read()
    cv2.imshow("text detected", Image)
    if cv2.waitKey(1) & 0XFF==ord('s'):
        cv2.imwrite(r'C:\Users\sanja\OneDrive\Documents\GitHub\NLP-OpenCV-Food-Labels\test.png', Image)

camera.release()
cv2.destroyAllWindows()

def tesseract():
    tesser_path = r"C:\Users\sanja\Downloads\tesseract-ocr-w64-setup-5.3.0.20221222.exe"
    Imagepath = "test.png"
    pytesseract.tesseract_cmd=tesser_path
    text = pytesseract.image_to_string(Image.open(Imagepath))
    print(text[:-1])
tesseract()
#img_path = r'C:\Users\sanja\OneDrive\Documents\GitHub\NLP-OpenCV-Food-Labels\nlp_diagram.png'
