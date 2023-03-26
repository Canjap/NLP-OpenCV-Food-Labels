import keras_ocr 
import os 

def pipelineProcessor():
    pipeline = keras_ocr.pipeline.Pipeline()

    # Get a set of three example images
    images = [
        keras_ocr.tools.read(image) for image in [r"images\200.png"]
    ]

    prediction_groups = pipeline.recognize(images)

    pred_img = prediction_groups[0]
    return_str = []
    for text, box in pred_img:
        return_str.append(str(text))
    return return_str
print(pipelineProcessor())