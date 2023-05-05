from flask import Flask, render_template, Response, request
import cv2
import datetime, time
import os, sys
import numpy as np
from threading import Thread
import pandas as pd 

from keras_text import pipelineProcessor
import keras_text
from find_return_nutrition_site import find_return_nutrition_site as frns
from find_return_nutrition_site import toCSVs
import file_manage

capture = False
label = False
off_on = 0
rec = 0

def gen(num):
    for i in range(num):
        yield str(i)

generator = gen(100)

images_path = fr'C:\Users\sanja\OneDrive\Documents\GitHub\NLP-OpenCV-Food-Labels\images\{next(generator)}.png'

generator = [x for x in range(100)]
#instatiate flask app  
app = Flask(__name__, template_folder='./templates')


camera = cv2.VideoCapture(0)

def record(out):
    global rec_frame
    while(rec):
        time.sleep(0.05)
        out.write(rec_frame)
 

def gen_frames():  # generate frame by frame from camera
    global out, capture,rec_frame, label 
    while True:
        success, frame = camera.read() 
        if success:
            if(capture):
                capture=False
                file_manage.deleteImages()
                cv2.imwrite(images_path, frame)
                global words
                words = keras_text.pipelineProcessor()
                print(words)
            if(label):
                toCSVs(frns(words))
                label = False
            try:
                ret, buffer = cv2.imencode('.jpg', cv2.flip(frame,1))
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                pass
                
        else:
            pass


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/requests',methods=['POST','GET'])
def tasks():
    global off_on,camera
    if request.method == 'POST':
        if request.form.get('click') == 'Capture':
            global capture
            capture=True
        elif  request.form.get('label') == 'Read Label':
            global label
            label=True
        elif  request.form.get('stop') == 'Stop/Start':
            
            if(off_on==1):
                off_on=0
                camera.release()
                cv2.destroyAllWindows()
                
            else:
                camera = cv2.VideoCapture(0)
                off_on=1
                          
                 
    elif request.method=='GET':
        return render_template('index.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    
camera.release()
cv2.destroyAllWindows()  