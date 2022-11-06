import time
import requests
from requests.auth import HTTPBasicAuth

DOMAIN = 'http://127.0.0.1'

def timeout():
    time.sleep(2)

def get_url(url):
    return f'{DOMAIN}{url}'

# timeout()
auth = HTTPBasicAuth(username='Admin', password='NewEntry1')
# doesn't authirised
# response = requests.get('http://127.0.0.1/api/users/', auth=auth)


# token authorisation
# data = {'username':'Admin', 'password':'NewEntry1'}
# token = requests.post('http://127.0.0.1/api-token-auth/', data=data).json().get('token')
# # token = response

# headers = {'Authorization':f'Token {token}'}
# response = requests.get(get_url('/api/users/'), headers=headers)

# print(response.json())

# JWT auth
data = {'username':'Admin', 'password':'NewEntry1'}
TOKEN = requests.post('http://127.0.0.1/api/token/', data=data).json()

# print(TOKEN)
access = TOKEN['access']
# print(access)
# print('*' * 40)
refresh = TOKEN['refresh']
# print(refresh)
# print('*' * 40)

headers = {'Authorization': f'Bearer {access}'}
response = requests.get(get_url('/api/users/'), headers=headers)
# print(response.json())

new_TOKEN = requests.post('http://127.0.0.1/api/token/refresh/', data={'refresh': refresh}).json()

# print(new_TOKEN)










