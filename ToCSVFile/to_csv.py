import pandas as pd 
import numpy as np 
import sys 
sys.path.append("C:\\Users\\sanja\\OneDrive\\Documents\\GitHub\\NLP-OpenCV-Food-Labels\\text_detection") # adds text_detection folder to list of modules/libs Python uses


words_list = ["apple", "cinammon", "cereal", "Nutrition", "Carbs", 230, "fats", 25]#keras_text.pipelineProcessor()
packaging_list = words_list[:words_list.index("Nutrition")] #text on the front of the package
nutrition_label = words_list[words_list.index("Nutrition"):] #nutrition facts/label text
''' 
organizing them into a dict makes creating the dataframe easier 
--> easier to send to Excel
would need to test using the pipelineProcessor function first before implementing
'''
data = {
    "Label" : [packaging_list],
    "Nutrition Label" : [nutrition_label]
    }
df = pd.DataFrame(data)

print(df)
