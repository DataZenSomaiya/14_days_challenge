import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=java&txtLocation=').text
soup = BeautifulSoup(result,'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    comp_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
    skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
    update_post = job.find('span',class_ = 'sim-posted').span.text

    print(f'Company Name : {comp_name.strip()}')
    print(f'Skills Required : {skills.strip()}')
    print(f'Post Updated on : {update_post}')

print('')




