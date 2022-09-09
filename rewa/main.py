from bs4 import BeautifulSoup
import requests
response = requests.get('https://en.wikipedia.org/wiki/India')
print(response.status_code)
src = response.content
soup = BeautifulSoup(src , 'lxml')
links = soup.find_all("a")
print(links)
for link in links :
    if "languages" in link.text :
        print(link)
        print(link.attrs['href'])
