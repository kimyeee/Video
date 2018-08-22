import requests

file = open('已去重复.txt', 'rb').readlines()
a, c = 0, 0
for txt in file:
    # print(txt)
    try:
        file_list = txt.decode('gbk').split('----')
        for word in range(len(txt)%4):

    except Exception as e:
        print(e)
        c += 1
    a += 1
    print(a)
    print(c)
    # print(file_list)
