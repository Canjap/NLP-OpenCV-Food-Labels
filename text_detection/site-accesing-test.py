import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.myfooddiary.com/foods/search?q=Tostitos+scoops+")
                 
soup = BeautifulSoup(r.content, "html.parser")

link = soup.find("a", {"class" : "lnkFoodDesc"})
new_link = link["href"]
new_r = requests.get("https://www.myfooddiary.com" + str(new_link))
soup = BeautifulSoup(new_r.content, "html.parser")

divs = soup.find(id = "FoodLabelHldr")

to_df = divs.text
to_df = to_df.splitlines()
to_df = [elem for elem in to_df if elem.strip()]
nono_words = ['Nutrition Facts', 'Amount Per Serving', '% Daily Value*', 'The % Daily Value (DV) tells you how much a nutrient in a serving of food contributes to a daily diet. 2,000 calories a day is used for general nutrition advice.']
for x in to_df:
    if x in nono_words:
        to_df.remove(x)
to_df[18] = to_df[18].strip()
to_df[-1] = to_df[-1].strip()
to_df.remove(to_df[0])

print(to_df)
for x in to_df:
    if x != to_df[-1]:
        if x.endswith('%') or x.endswith("0"):
            to_df[to_df.index(x)+1] += f" {x}"
            to_df.remove(x)
    else:
        break

name =[]
mg = []
percents = []
for x in to_df:
    x = x.split()
    print(x)