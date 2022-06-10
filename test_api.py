import requests
import json

import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=c26c7ea6ddaa4806a0e5cd20d433223d')
response = requests.get(url)
data = response.json()

data_list = []
for i in data['articles']:
    data_list.append(i)

print(data_list[3]['content'])
