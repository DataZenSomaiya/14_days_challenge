import requests

from bs4 import BeautifulSoup

# Making a get request
response = requests.get('https://www.instagram.com/')
response1 = requests.get('https://www.facebook.com/')
# print response
print(response)
print(response1)
# print url
print(response.url)
print(response1.url)