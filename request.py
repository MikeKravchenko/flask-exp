import requests
session = requests.Session()
print(session.cookies.get_dict())

response = session.get('http://simon0.mkravchenko.in.mlaas.net/data')
print(session.cookies.get_dict())


и чё дальше?
