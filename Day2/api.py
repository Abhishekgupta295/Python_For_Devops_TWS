import requests

myurl = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url = myurl)

print(response.json())
print(type(response.json()))