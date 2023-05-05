import requests
from bs4 import BeautifulSoup
import pandas as pd 
from itertools import zip_longest


r = requests.get(f"https://www.myfooddiary.com/foods/4029949/kelloggs-apple-cinnamon-nutri-grain-bar")
soup = BeautifulSoup(r.content, "html.parser")

divs = soup.find(id = "FoodLabelHldr")

to_df = divs.text
to_df = to_df.splitlines()
to_df = [elem for elem in to_df if elem.strip()]
print(to_df)
print(to_df)
for x in to_df:
    if x != to_df[-1]:
        if x.endswith('%'):
            to_df[to_df.index(x)+1] += f" {x}"
            to_df.remove(x)
    else:
        break

#print(to_df)

to_df = [elem.split() for elem in to_df]
for elem in to_df:
    if len(elem) == 4:
        elem[0] = elem[0] + " " + elem[1]
        elem.remove(elem[1])
    
#print(to_df)
names = [elem[0] for elem in to_df]
print(names)
mg = []
for elem in to_df:
    for ind in elem:
        if ind.endswith('g'):
            mg.append(ind)
print(mg)
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

d = {'amt per serving' : names, 'mg' : mg, "percents" : percents}
print(len(mg), len(percents), len(names))

df = pd.DataFrame(data=d)
print(df)