# myfile = open('test.mp4','a')
# myfile.write("####&&&&")
import hashlib
import os
import datetime


def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


print(GetFileMd5('ttt.mp4'))
print(GetFileMd5('ttt1.mp4'))
