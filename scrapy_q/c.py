import requests

res = requests.get('http://www.tianyashuku.com/kehuan/1440/')
print(res.content.decode('utf8'))
