import keras_ocr 
import matplotlib.pyplot as plt
import os 

pipeline = keras_ocr.pipeline.Pipeline()

# Get a set of three example images
images = [
    keras_ocr.tools.read(image) for image in [r"images\200.png"]
]

prediction_groups = pipeline.recognize(images)

pred_img = prediction_groups[0]

for text, box in pred_img:
    print(text)