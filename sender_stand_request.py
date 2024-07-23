import configuration
import requests
import data

#def get_docs():
    #return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,params={"count": 20})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USER_TABLE_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def post_products_kits(product_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                        json=product_ids,  # inserta el cuerpo de solicitud
                        headers=data.headers)  # inserta los encabezados

response = get_users_table()
#print(response.status_code)
#print(response.headers)
#print(response.text)

#response_logs= get_logs()
#print (response_logs.status_code)

response_new_user= post_new_user(data.user_body)
print(response_new_user.status_code)
print(response_new_user.json())

#response_product_ids= post_products_kits(data.product_ids)
#print(response_product_ids.status_code)
#print(response_product_ids.json())
