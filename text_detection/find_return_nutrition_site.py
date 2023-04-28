import requests
from bs4 import BeautifulSoup
import pandas as pd
def find_return_nutrition_site(*words): #has list like attrs
    global list_words
    list_words = [word for word in words]
    r = requests.get(f"https://www.myfooddiary.com/foods/search?q={'+ '.join([str(x) for x in [*list_words]])}")
                    
    soup = BeautifulSoup(r.content, "html.parser") #uses bs4 to parse thru html

    link = soup.find("a", {"class" : "lnkFoodDesc"}) #finds the first instance of a link with the specified class
    new_link = link["href"] #accesses the link
    new_r = requests.get("https://www.myfooddiary.com" + str(new_link)) #creates new link; basically clicks the link
    soup = BeautifulSoup(new_r.content, "html.parser") #parses thru new link's html

    divs = soup.find(id = "FoodLabelHldr") #this div has the divs containing the nutrition info

    to_df = divs.text #outputs text found in html
    to_df = to_df.splitlines() #splits this into new lines; seperates the rows
    to_df = [elem for elem in to_df if elem.strip()] #returns truncated list of nutrition info
    nono_words = ['Nutrition Facts', #list of unnessary words
                  'Amount Per Serving', 
                  '% Daily Value*', 
                  'The % Daily Value (DV) tells you how much a nutrient in a serving of food contributes to a daily diet. 2,000 calories a day is used for general nutrition advice.']
    for x in to_df: #removes unnes words
        if x in nono_words: 
            to_df.remove(x)
    to_df[18] = to_df[18].strip() #takes away extra chars
    to_df[-1] = to_df[-1].strip() #takes away extra chars
    to_df.remove(to_df[0]) #takes away extra chars
    num_cals = to_df.pop(0)
    calories = to_df.pop(0)
    to_df.remove(to_df[-1])
    to_df.remove(to_df[-1])

    for x in to_df: #loops thru list
        if x != to_df[-1]: #avoids index out of bounds error
            if x.endswith('%') or x.endswith("0"): #checks if the elem is either a percent of number
                to_df[to_df.index(x)+1] += f" {x}" #switches the elems
                to_df.remove(x) #takes original elem out
        else: #stops when last index reached
            break 
    
    to_df = [elem.split() for elem in to_df]
    for elem in to_df:
        if len(elem) == 4:
            elem[0] = elem[0] + " " + elem[1]
            elem.remove(elem[1])

    names = [elem[0] for elem in to_df]
    mg = []
    for elem in to_df:
        for ind in elem:
            if ind.endswith('g'):
                mg.append(ind)
    percents = []
    for elem in to_df:
        count = 0
        for ind in elem:
            if "%" in ind:
                percents.append(ind)
                count += 1
        if count == 0:
            percents.append(None)
    names.insert(0, calories)
    mg.insert(0, num_cals)
    percents.insert(0, None)
    d = {'name' : names, 'amounts' : mg, "percents" : percents}

    df = pd.DataFrame(data=d)
    return df

def toCSVs(df):
    df.to_csv(fr"text_detection\food_CSVs\{list_words[0]}.csv", encoding="utf-8", index=False)
