from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html,"html.parser")
base_url = "http://olympus.realpython.org"

for link in soup.find_all("a"):
    link_url = base_url + link["href"]
    print(link_url)