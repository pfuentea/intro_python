import requests
import json 

#crearemos un metodo para las solicitudes

def solicitudes(metodo,headers,payloads,user_id=0):
    url="https://reqres.in/api/users"
    if metodo=="PUT" or metodo=="DELETE":
        url+="/"+str(user_id)
    
    respuesta=requests.request(metodo,url,headers=headers, data=payloads)
    if metodo=="DELETE":
        return respuesta.status_code

    return json.loads(respuesta.text)

#requerimiento 1: imprimir info por pantalla , SELECT=GET
# users_data =solicitudes('GET',{},{})
# print(users_data)

#requerimiento 2: crear=POST
data={
    "name": "Ignacio",
    "job": "Profesor"
}
# created_user =solicitudes('POST',{},data)
# print(created_user)

#requerimiento 3: modificar=PUT
data={
    "name": "Morpheus",
    "residence": "Zion"
}
headers = {
    "Content-Type": "application/json"
}
json_data = json.dumps(data)
#headers = {'Authorization': 'Bearer your_token'}
# updated_user =solicitudes('PUT',headers, json_data)
# print(updated_user)

#requerimiento 4:
data={
    "name": "Tracey",
}
json_data = json.dumps(data)
deleted_user =solicitudes('DELETE',headers, json_data,6)
print(deleted_user)