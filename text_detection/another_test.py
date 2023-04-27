import requests
from bs4 import BeautifulSoup
import pandas as pd


to_df = [['Total Fat', '3.5g', '5%'], ['Saturated Fat', '0.5g', '3%'], ['Trans', 'Fat', '0g'], ['Cholesterol', '0mg', '0%'], ['Sodium', '125mg', '5%'], ['Total Carbohydrate', '25g', '8%'], ['Dietary Fiber', '1g', '4%'], ['Total', 'Sugars', '13g'], ['Includes', '12g', 'Added', 'Sugars', '24%'], ['Protein', '2g'], ['Vitamin D', '0mcg', '0%'], ['Calcium', '100mg', '8%'], ['Iron', '1.8mg', '10%'], ['Potassium', '0mg', '0%'], ['Vitamin A', '25mcg', '3%'], ['Vitamin C', '0mg', '0%']]
percents = []

for elem in to_df:
    count = 0
    for ind in elem:
        if "%" in ind:
            percents.append(ind)
            count += 1
    if count == 0:
        percents.append(None)
print(percents)