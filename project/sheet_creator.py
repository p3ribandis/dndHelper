import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "http://tentaculus.ru/archive/tables/100_grave_things.html"
r = requests.get(URL_TEMPLATE)
print(r.status_code)
print(r.text)