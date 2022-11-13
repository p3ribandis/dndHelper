import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from sheets import pygsheetsExt as pyg

URL_TEMPLATE = "http://tentaculus.ru/archive/tables/useless_magic_items.html"
r = requests.get(URL_TEMPLATE)
r.encoding = 'utf8'

soup = bs(r.text, "html.parser")
sheet_content = soup.find_all('td')
sheet_name = soup.find('h1') 
for i in range(1, len(sheet_content), 2):
    print(sheet_content[i].text)

#pyg.set_new_worksheet(sheet_name.text, sheet_content)
