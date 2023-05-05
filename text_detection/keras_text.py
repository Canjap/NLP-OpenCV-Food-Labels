import keras_ocr 
import os 
import requests

def pipelineProcessor():
    pipeline = keras_ocr.pipeline.Pipeline()

    # Get a set of three example images
    images_folder = [image for image in os.listdir("images")]
    images = []
    for img in images_folder:
        images.append(keras_ocr.tools.read(f"images\\{img}"))
    return_str = []
    prediction_groups = pipeline.recognize(images)
    for img in range(len(prediction_groups)):
        pred_img = prediction_groups[img]
        for text, box in pred_img:
            return_str.append(str(text))
    return " ".join(return_str)

