from bs4 import BeautifulSoup
import requests

url = "https://www.91mobiles.com/compare-mobile-phones.html"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
tags = doc.find_all("div", class_="compare-mob-price")
names = doc.find_all("div", class_="m-name")

t = []
for tag in tags:
    tag = tag.string.replace(" ", "")
    t.append(tag)

n = []
for name in names:
    name = name.string.replace(" ", "")
    n.append(name)

for mobile in range(0, 4):
    print("Name of mobile " + str(n[mobile]) + "\nPrice is " + t[mobile])
