
import requests

# Using GET requests
# url = 'https://httpbin.org/get'
# payload = {'page': 2, 'count': 25}
# r = requests.get(url, params=payload)

# Using POST requests
url = 'https://httpbin.org/post'
payload = {'username': 'Luis', 'password': 'testing'}
r = requests.post(url, data=payload)

# print(r.text)

# Save JSON response
r_dict = r.json()
print(r_dict['form'])

# Basic Auth
url = 'https://httpbin.org/basic-auth/luis/testing'
r = requests.get(url, auth=('luis', 'testing'))    # Auth params passed as tuple
print(r.status_code)
print(r.text)