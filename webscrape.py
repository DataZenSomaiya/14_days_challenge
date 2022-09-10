# step 1 : get the libraries requests,html5,bs4
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# step 1 : get the html
r = requests.get(url)
htmlContent = r.content
print(htmlContent)

# step 2 : parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

# step 3 : html tree traversal
# 1. Tag
# 2. Navigable String
# 3. Beautifulsoup
# 4. comments

# Get the title of the HTMl page
title = soup.title
print(type(soup))
print(type(title))
print(type(title.string))

# Get all the paras of the HTMl page
paras = soup.find('p')
print(paras)

print(soup.find('p'))

print(soup.find('p')['class'])

print(soup.find_all("p", class_="lead"))

# Get Text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

# Get all the anchors of the HTMl page
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        linkText="https://codewithharry.com"+link.get('href')
        all_links.add(link)
        print(linkText)

navbarSupportedContent = soup.find(id='nav-content')

for elem in navbarSupportedContent.contents:
    print(elem)

for item in navbarSupportedContent.stripped_strings:
    print(item)
