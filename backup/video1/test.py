import requests
res = requests.get('https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js')
open(r'C:\Users\admin\PycharmProjects\Video\static\js\bootstrap.min.js','wb').write(res.content)