import requests
import lxml
from bs4 import BeautifulSoup

import config_nike

HOST = "https://https://www.nike.com/"
URL = "https://www.nike.com/w/jordan-1-aj85g"

HEADERS = config_nike.HEADERS


def get_html(URL, HEADERS, parama=""):
    response = requests.get(URL, headers=HEADERS, params=parama)
    return response

def get_content(html):
    soup = BeautifulSoup(html, "lxml")
    items = soup.find_all("div", class_="product-card product-grid__card css-c2ovjx")
    jordan = []

    for item in items:
        jordan.append(
            {
            "title": item.find("div", class_="product-card__body").find("a").get_text(strip=True),
            "link": item.find("div", class_="product-card__body").find("a").get("href"),
            'category': item.find('div', class_='product-card__body').find('div', class_='product-card__subtitle').get_text(),
            "price": item.find("div", class_="product-card__price").get_text(strip=True),
            # "ing": item.find("div", class_="image").find("img").get("src")
        }
        )
    return jordan

html= get_html(URL=URL, HEADERS=HEADERS)
content= get_content(html.text)

# with open ("html_nike.txt", "w") as f:
#     f.write(str(content))

def prs(content):
    items = []
    for ind, item in enumerate(content):
        items.append(f'''Товар №: {ind +1} Название: {item['title']}\nСсылка на товар: {item['link']}\nКатегория: {item['category']}\nЦена: {item['price']}\n------------\n''')
    return items
shoes = prs(content)


