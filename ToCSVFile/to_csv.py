import pandas as pd 
import numpy as np 
import sys 
sys.path.append("C:\\Users\\sanja\\OneDrive\\Documents\\GitHub\\NLP-OpenCV-Food-Labels\\text_detection") # adds text_detection folder to list of modules/libs Python uses
import keras_text

words_list = keras_text.pipelineProcessor()

data = {
    "Words" : words_list,
    }
df = pd.DataFrame(data)

print(df)