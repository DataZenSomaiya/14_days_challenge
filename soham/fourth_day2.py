from bs4 import BeautifulSoup
import requests
url = "https://www.geeksforgeeks.org/what-is-data-analysis/"
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")
tag = doc.find_all("strong")
print(len(tag))
for tags in tag[:10]:
    print(tags.string)


