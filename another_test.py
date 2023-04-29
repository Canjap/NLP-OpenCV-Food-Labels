import requests
from bs4 import BeautifulSoup
import pandas as pd

a = [1, 'a', 3, 'b']
print(f"unpack a list: {', '.join([str(x) for x in [*a]])}")