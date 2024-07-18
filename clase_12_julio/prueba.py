import requests
import json 
from string import Template

def request_get():
    url="https://aves.ninjas.cl/api/birds"
    return json.loads(requests.get(url).text)

def contenido():
    table_template = Template('''<table>
    <thead><tr><th>Nombre español</th><th>Nombre Inglés</th><th>Imagen</th></tr></thead>
    <tbody>
    $tbody
    </tbody>
    </table>
    ''')
    birds = request_get()
    tbody = ""
    for bird in birds:
        tbody+=f"<tr><td>{bird['name']['spanish']}</td><td>{bird['name']['english']}</td><td><img src=\"{bird['images']['thumb']}\"></td></tr>"

    return table_template.substitute(tbody = tbody)

html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <meta charset="UTF-8">
                            <title>Título de la Página</title>
                            </head>
                            <body>
                            <h1>Nuestra página Web</h1>
                        
                            $body

                            </body>
                            </html>
                        ''')

html=html_template.substitute(body = contenido())

with open('output.html', 'w') as f:
    f.write(html)