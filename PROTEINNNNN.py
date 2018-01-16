__author__ = 'mittr'

from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup
import re
import operator
import urllib.request as urllib2


def whey(self):
    # Let's fetch the soup for the page here!
    my_url = 'https://www.amazon.in/Optimum-Nutrition-Standard-Protein-Powder/dp/B000QSNYGI/ref=sr_1_6?s=hpc&ie=UTF8&qid=1516012071&sr=1-6&keywords=whey+protein'

    uClient = ureq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = Soup(page_html, "html.parser")

    # A little bit of Regex here to fetch the list items with id's beginning with flavor_name_
    containers = page_soup.findAll("li", {"id": re.compile("^flavor_name_")})

    while True:
        try:
            # The solution set :)
            dictionary = {}
            for container in containers:
                print(container['title'][15:], '\t', container['data-dp-url'])
                if not container['data-dp-url']:
                    price = page_soup.find("span", {"id": "priceblock_ourprice"})
                    dictionary[str(container['title'][15:].strip())] = float(price.text.replace(u'\xa0', u' ').replace(',', '').strip())

                # now go to the link to fetch the price and store in the dictionary
                else:
                    uCl = ureq('https://www.amazon.in/Optimum-Nutrition-Standard-Protein-Powder' + container['data-dp-url'])
                    html = uCl.read()
                    uCl.close()
                    soup = Soup(html, "html.parser")
                    price = soup.find("span", {"id": "priceblock_ourprice"})
                    dictionary[str(container['title'][15:].strip())] = float(price.text.replace(u'\xa0', u' ').replace(',', '').strip())
        except urllib2.HTTPError as err:
            print("RESTARTING - NETWORK ERROR")
            pass
        else:
            break
    print("Flavors in non-descending order of price: \n")


    # Sorting the dictionary items in non decreasing order!

    sorted_x = sorted(dictionary.items(), key=operator.itemgetter(1))
    print(sorted_x)
    print(len(sorted_x))

    for flavor, price in sorted_x:
        print("{:<25} {:<7}".format(flavor, price))
