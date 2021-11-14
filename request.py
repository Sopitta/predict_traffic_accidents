import requests

#url = 'http://localhost:5000/api'
url = 'http://localhost:5000'
r = requests.post(url,json={'Category':'Alkoholunfälle','Type':'insgesamt','Year':'2021','Month':'01'})
print(r.json())