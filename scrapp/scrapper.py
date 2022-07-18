import requests # python3 -m pip install requests beautifulsoup4
from bs4 import BeautifulSoup
from models.product import products
from config.db import conn


url = "https://webscraper.io/test-sites/e-commerce/allinone"

def scrapp():
    lista = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    def has_data_search(tag):
        return tag.find("div", attrs={"class": "thumbnail"})

    results = soup.find_all(has_data_search) 

    for prod in results:
        try:
            name = prod.find("a", attrs={"class": "title"})['title']
            description = prod.find("p", attrs={"class": "description"}).get_text()
            pri = prod.find("h4", attrs={"class": "pull-right price"}).get_text()
            pri = pri.replace("$","")
            price = float(pri)

            new_product = {"name": name, "description": description, "price": price}
            if new_product not in lista:
                lista.append(new_product)

        except Exception as e:
            print("Exception: {}".format(e))
            pass
    
    for i in lista:
        conn.execute(products.insert().values(i))