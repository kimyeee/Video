import requests
res = requests.get('https://code.jquery.com/jquery-3.3.1.min.js')
open(r'C:\Users\admin\PycharmProjects\Video\static\js\jquery-3.3.1.min.js','wb').write(res.content)