#R1: Importación de Librerias
import requests
import json
from string import Template
#R2: Función
def request_get(url):
    return json.loads(requests.get(url).text)
#R3: Obtencion de data
jsondata = request_get('https://aves.ninjas.cl/api/birds')
#R4: Obtención de dato de estudio
datos = [{"name_sp": bird["name"]["spanish"], "name_en": bird["name"]["english"], "image": bird["images"]["main"]} for bird in jsondata]
#R5: Creación de HTML
img_template = Template('<td><img src="$url" width="182" height="200"><p>$name_sp</p><p>$name_en</p></td>')
html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <title>Aves de chile</title>
                            </head>
                            <body>
                            <h1>Aves de chile</h1>
                            <table> $body </table>
                            </body>
                            </html>
                        ''')
#R6: Generación de imagenes HTML
lista_img = [img_template.substitute(url = elemento['image'], name_sp = elemento['name_sp'], name_en = elemento['name_en']) for elemento in datos]
#R7: Imagenes por filas
texto_img = ''
nfigCol = 7 
for i in range(0, len(lista_img), nfigCol): 
    texto_img += '<tr>' + ''.join(lista_img[i:i+nfigCol]) + '</tr>\n'
#R8: HTML final
html = html_template.substitute(body = texto_img)
print(html)
#R9: HTML en un archivo
with open('prueba.html', 'w') as f:
    f.write(html)
