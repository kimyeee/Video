import hashlib

import requests

res = requests.get('http://bdmov.a.yximgs.com/upic/2018/08/22/22/BMjAxODA4MjIyMjA4MTlfMjkxOTg5MDhfNzcyMDA5MDk5OF8xXzM=_b_B65bd42b3b88f4d05847ff449ce14e4c4.mp4')
# res.content
myhash = hashlib.md5()
f = res.content
f1 = res.content+b'####&&&&'

myhash.update(f1)
open('ttt.mp4','wb').write(f)
open('ttt1.mp4','wb').write(f1)