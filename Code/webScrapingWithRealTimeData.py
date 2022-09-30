from unittest import result
import mechanicalsoup
import time

browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of the dice roll is : {result}")
    if i < 3:    
        time.sleep(10)

