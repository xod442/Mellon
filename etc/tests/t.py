import requests

s = requests.Session()
data = {"username":"admin", "password":"admin"}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
url = "http://10.132.0.76/admin/launch?script=rh&template=json-request&action=json-login"
r = s.post(url, data=data, headers=headers)
print(r.text)
