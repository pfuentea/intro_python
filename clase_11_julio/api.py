import requests
import json 
url_base="https://swapi.dev/api"
url_planetas=url_base+"/planets/"

payloads={}
headers={}

response = requests.request('GET',url_planetas,headers=headers, data=payloads)

resultados=json.loads(response.text)
planetas=resultados['results']
# por ejemplo para generar la data para un CSV
for p in planetas:
    print(f"{p['name']};{p['diameter']};{p['rotation_period']}")

#print(resultados['count'])