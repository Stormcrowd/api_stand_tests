import configuration
import requests
import data


#EJERCICIO 5

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, headers=data.headers, json=products_ids)

response = post_products_kits(data.product_ids)
print(response.status_code)
print(response.json())

#Ejercicio 4:

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

#EJERCICIO_3 RECUPERAR INFORMACION DE TABLA DE DATOS
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()
print(response.status_code)

#EJERCICIO_2  LOGS DEL SERVIDOR PRINCIPAL

#def get_logs():
    #return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":20})

#response = get_logs()
#print(response.headers)
#print(response.status_code)

#EJERCICIO_1 SOLICITUD BASE

#def get_docs():
    #return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


#response = get_docs()
#print(response.text)