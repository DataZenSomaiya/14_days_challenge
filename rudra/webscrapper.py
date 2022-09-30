import requests
from bs4 import BeautifulSoup



r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

soup = BeautifulSoup(r.content, 'html.parser')


s = soup.find('div', id= 'main')


leftbar = s.find('ul', class_='leftBarList')


content = leftbar.find_all('li')

print(content)
