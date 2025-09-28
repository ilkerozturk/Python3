import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/')

allData = response.json()


for i in allData:
    print(i['userId'],i['title'])