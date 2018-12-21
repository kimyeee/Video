import os

from scrapy_q.book.book.settings import MEDIA_ROOT

all_count = list(os.walk(MEDIA_ROOT))[0]

for i in all_count[1]:
    print(i)
    print(MEDIA_ROOT + '\\' + i)
    read_dir_path = 'E:\SOME\备份\小说\\'
    write_dir_path = 'E:\SOME\备份\小说_全本\\'
    l = os.listdir(MEDIA_ROOT + '\\' + i)
    for part in sorted(l, key=lambda x: int(x.split('.')[0])):
        print(part)
        txt_path = r'%s\%s\%s' % (read_dir_path, i, part)
        txt = open(txt_path, 'r').read()
        print(txt)
        break

        # print(sorted(l,key=lambda x:int(x.split('.')[0])))
    break
