from bs4 import BeautifulSoup
import requests
t = []
p = []
url = "https://www.ranker.com/list/best-action-anime/ranker-anime"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
tags = doc.find_all("a", class_="listItem_name__Qq_Y8 listItem_nameLink__eLagT")[:5]
release = doc.find_all("div", class_="listItem_firstProperties__C0pzn")[:5]

for tag in tags:
    a = tag.text
    t.append(a)


for taggs in release:
    b = taggs.text
    p.append(b)


print("ACTION ANIMES :")
for anime in range(len(t)):
    print(t[anime] + "  :  " + p[anime])
 