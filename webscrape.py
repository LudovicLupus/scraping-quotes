# Scraping from quotes.to.scrape.com
import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

# Returns requests objects
def fetchSite(site):
    r = requests.get(site)
    print(f'Encoding: {r.encoding}')
    return r


r = fetchSite(url)  # Requests objects
soup = BeautifulSoup(r.text, 'html.parser')     # Create soup object from html

# print(soup.prettify())

# Throw all <a> tags in a list
aList = []
for a in soup.find_all('a'):
    aList.append(a)

print(f'Length of aList: {len(aList)}')     # Using f-strings here for formatting (the Python3 way)
print(aList)