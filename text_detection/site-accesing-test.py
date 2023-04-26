import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.myfooddiary.com/foods/search?q=Tostitos+scoops+")
                 
soup = BeautifulSoup(r.content, "html.parser")

link = soup.find("a", {"class" : "lnkFoodDesc"})

print(link["href"])
