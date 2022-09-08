from bs4 import BeautifulSoup
import requests

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

print(doc.prettify())  # prettify()->>indentation ke liye

tag = doc.h1  # particular tag dundne ke liye
tag.string = "hello"##h1 ko change kar diya
print(tag)

tag1=doc.find_all("h3")##saare tags find karne ke liye
print(tag1)

tag2=doc.find_all("title")[0]
print(tag2.find_all("h2"))##for finding nested tags

url="https://www.instagram.com/alihealth_1/?hl=en"

result=requests.get(url)
doc=BeautifulSoup(result.text,"html.parser")##storing page ka html in variable
print(doc.prettify())






