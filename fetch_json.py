
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

postId, id_field, name, email, body = ([] for i in range(5))

for i in data:
    postId.append(i["postId"])
    id_field.append(i["id"])
    name.append(i["name"])
    email.append(i["email"])
    body.append(i["body"])

df = pd.DataFrame({'A': postId,
                   'B': id_field,
                   'C': name,
                   'D': email,
                   'E': body})

print(df.head())
