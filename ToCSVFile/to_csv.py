import pandas as pd 
import numpy as np 
import sys 
sys.path.append("C:\\Users\\sanja\\OneDrive\\Documents\\GitHub\\NLP-OpenCV-Food-Labels\\text_detection") # adds text_detection folder to list of modules/libs Python uses
import keras_text

words_list = ["apple", "cinammon", "cereal", "Nutrition"]#keras_text.pipelineProcessor()
nutrion_label = " ".join(words_list).split("Nutrition")
data = {
    "Label" : [words_list],
    #"Nutrition Label" : 

    }
df = pd.DataFrame(data)

print(df)