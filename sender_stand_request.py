import configuration
import requests
import data

#Petición para crear usuario
def post_new_user (user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=user_body,
                        headers=data.headers)

response = post_new_user(data.user_body)

#print(response)
#print(response.text)
#print(response.content)
#print(response.json()["authToken"])


auth_token =(response.json()["authToken"])
headers = data.headers.copy()
headers["Authorization"] = f"Bearer  + {auth_token}"
#print(headers)
def post_new_client_kit (kid_body, auth_token):
    reply_user = data.headers.copy()
    reply_user["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kid_body,
                         headers=reply_user
                         )

response = post_new_client_kit(data.kit_body,auth_token)
print(response.content)