
from bs4 import BeautifulSoup
import requests
t = []
p = []
url = "https://www.91mobiles.com/top-10-mobiles-in-india"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
tags = doc.find_all("a", class_="hover_blue_link name gaclick")[:5]
prices = doc.find_all("span", class_="price price_padding")[:5]

for tag in tags:
    a = tag.text.replace(" ", "")
    t.append(a)

for price in prices:
    b = price.text.replace(" ", "")
    p.append(b)

print("Name and price of top 5 phones are :")
for mobile in range(len(t)):
    print(t[mobile] + "  :  " + p[mobile])
