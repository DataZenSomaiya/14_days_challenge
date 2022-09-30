
from bs4 import BeautifulSoup

with open("html.html", "r") as f:
    doc = BeautifulSoup(f,  "html.parser")
tag = doc.find("title")
print(tag.string)
