import requests
import sys

url ="https://jsonplaceholder.typicode.com/posts"
res = requests.get(url)

if res.status_code != 200:
    sys.exit(1)
data= res.json()
print(type(data))
print(type(data[0]))    