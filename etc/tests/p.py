import requests
import json
host = '10.132.0.76'
s = requests.Session()
url = 'http://'+host+'/admin/launch'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

params = {
    'script': 'rh',
    'template': 'json-request',
    'action': 'json-login',
}

data = {"username": "admin","password": "admin"}
data= json.dumps(data)

response = s.post(url, params=params, headers=headers, data=data)
client_dict = s.cookies.get_dict()
session_key = client_dict['session']
key = 'session=' + session_key


##
#   USe session key to get show command
#

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'cookie': key
}

params = {
    'script': 'json',
}

data = {"cmd": "show interfaces ethernet 1/16"}
data= json.dumps(data)

response = s.post('http://10.132.0.76/admin/launch', params=params, headers=headers, data=data)



print(response.text)
print("------------------------------------------------------------")
print(response.headers)
print("------------------------------------------------------------")
print(key)
# print(type(s.cookies.get_dict()))
