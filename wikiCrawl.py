# Creating simple Wikipedia webcrawler

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Random_forest'

r = requests.get(url)
print(f'Status Code: {r.status_code}')
print(f'Encoding: {r.encoding}')

# Creating the BeautifulSoup parsed tree
soup = BeautifulSoup(r.text, 'html.parser')

# Using a tag name (e.g. 'a') as an attribute returns only
# the first tag by that name
print(f"This is soup.a: {soup.a}")
print(f"This is soup.a.name: {soup.a.name}")
print(f"This is soup.a['id']: {soup.a['id']}")

# Navigating all tags with a certain name using find_all
# print(soup.find_all('a')[2])
# Find all href links within <a> tags
# for link in soup.find_all('a'):
#     print(link.get('href'))

# Tags' children are available in a list called .contents
print("Profiling object types:\n")
print(f"THIS IS soup:\n {type(soup)}")                                                      # <class 'bs4.BeautifulSoup'>
print(f"THIS IS soup.body:\n {type(soup.body)}")                                            # <class 'bs4.element.Tag'>
print(f"THIS IS soup.body.find_all('div')):\n {type(soup.body.find_all('div'))}")           # <class 'bs4.element.ResultSet'>
print(f"THIS IS soup.body.find_all('div')[3]):\n {type(soup.body.find_all('div')[3])}")     # <class 'bs4.element.Tag'>

print("\n")
# PENDING: How to navigate tag tree


# print(f"tag_p: {tag_p}")
#
# for child in tag_p.children:
#     print(child.descendants)

# /html/body/div[3]/div[3]/div[4]/div/p[1]




