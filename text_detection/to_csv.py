import pandas as pd 
import numpy as np 
import sys 
sys.path.append("C:\\Users\\sanja\\OneDrive\\Documents\\GitHub\\NLP-OpenCV-Food-Labels\\text_detection\\keras_text.py") # adds text_detection folder to list of modules/libs Python uses
import keras_text

words_list = keras_text.pipelineProcessor()
packaging_list = words_list[:words_list.index("Nutrition")]
nutrition_label = words_list[words_list.index("Nutrition"):]
data = {
    "Label" : [packaging_list],
    "Nutrition Label" : [nutrition_label]
    }
df = pd.DataFrame(data)

print(df)