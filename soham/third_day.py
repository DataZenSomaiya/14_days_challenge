from bs4 import BeautifulSoup
import requests
url = "https://en.wikipedia.org/wiki/Data_Analysis"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

words = doc.find_all(text="data cleaning")
parent = words[0].parent
print(parent)
