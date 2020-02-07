
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

pd.set_option('display.max_columns', 10)

url = 'https://jsonplaceholder.typicode.com/comments/'

r = requests.get(url)       # Response
data = json.loads(r.text)
print(f'Type(data): {type(data)}')
keys = data[0].keys()
print(f'Keys: {keys}')

postId, id_field, name, email, body = ([] for i in range(5))    # Declare multiple empty lists using list comprehensions

for i in data:  # Data is a list (each item is a dict object)
    postId.append(i.get("postId"))  # Create individual series per attribute
    id_field.append(i.get("id"))    # dict.get returns None if key not found
    name.append(i.get("name"))
    email.append(i.get("email"))
    body.append(i.get("body"))

df = pd.DataFrame({'A': postId,
                   'B': id_field,
                   'C': name,
                   'D': email,
                   'E': body})

print(df.head())

# import pdb
# pdb.set_trace()
# print(df.headd)
