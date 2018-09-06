import os

file_list = os.listdir(os.getcwd())
file_list.remove(__file__.split('/')[-1])
for file in file_list:
    open(file, 'ab').write(b'####&&&&')
print(file_list)
