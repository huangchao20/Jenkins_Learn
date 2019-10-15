import os

def Remove(dpath):
    if os.path.isfile(dpath):
        print("回收文件[%s]" %dpath)
    elif os.path.isdir(dpath):
        print("[%s]目录暂时无法回收" % dpath)
    else:
        print('这个真整不了')
