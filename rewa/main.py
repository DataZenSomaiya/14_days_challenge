# import requests module
import requests

# Making a get request
response = requests.get('http://api.github.com')

# print response
print(response)

# print url
print(response.url)