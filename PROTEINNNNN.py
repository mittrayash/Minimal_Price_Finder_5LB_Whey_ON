__author__ = 'mittr'

from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup
import re

my_url = 'https://www.amazon.in/Optimum-Nutrition-Standard-Protein-Powder/dp/B000QSNYGI/ref=sr_1_6?s=hpc&ie=UTF8&qid=1516012071&sr=1-6&keywords=whey+protein'

uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = Soup(page_html, "html.parser")

containers = page_soup.findAll("li", {"id": re.compile("^flavor_name_")})

print(len(containers))

for container in containers:
    print(container['title'][15:])
