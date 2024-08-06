from campaña import Campaña
from anuncio import Video
from datetime import datetime

def guardar_log(texto):
    with open("logs.txt",'a+') as archivo: # w: write, r: read
        now=datetime.now()
        archivo.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {texto}\n")
    archivo.close()

try:
    c1=Campaña('campaña 1','01-08-2024','19-09-2024')
    v1=Video(5)
    c1.add_anuncio(v1)
    print(c1)
except Exception as e:
    guardar_log(str(e))