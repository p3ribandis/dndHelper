import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "http://tentaculus.ru/archive/tables/100_grave_things.html"
r = requests.get(URL_TEMPLATE)
r.encoding = 'utf8'

soup = bs(r.text, "html.parser")
sheet_content = soup.find_all('td')
for i in range(1, len(sheet_content), 2):
    print(sheet_content[i].text)