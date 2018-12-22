import os

from scrapy_q.book.book.settings import MEDIA_ROOT

all_count = list(os.walk(MEDIA_ROOT))[0]
read_dir_path = 'E:\SOME\备份\小说\\'
write_dir_path = 'E:\SOME\备份\小说_全本\\'

for i in all_count[1]:
    print(MEDIA_ROOT + '\\' + i)
    part_list = os.listdir(MEDIA_ROOT + '\\' + i)
    if len(part_list) > 2:
        part_list = sorted(part_list, key=lambda x: int(x.split('.')[0]))
    write_path = r'%s%s.txt' % (write_dir_path, i)
    print(write_path)
    with open(write_path, 'w') as write_f:
        for part in part_list:
            print(part)
            txt_path = r'%s\%s\%s' % (read_dir_path, i, part)
            txt = open(txt_path, 'r').read()
            print(txt.replace('None', '暂无'))
            write_f.write(txt.replace('None', '暂无') + '\r\n\r\n')
            # break

    # break
