import os
i = 0
j = 0
t = 0
def joinStr(path):
    global i
    global j
    global t
    if os.path.isdir(path):
        print('这个绝壁是目录')
        j += 1
        for d in os.listdir(path):
            newfile = os.path.join(path, d)
            print('-----------------------[%s]--------------------' % newfile)
            joinStr(newfile)
    elif os.path.isfile(path):
        print("文件名：【%s】" %path)
        i += 1
    else:
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        t += 1

if __name__ == '__main__':
    path = 'G:\\黄大宝python\\2018'
    joinStr(path)
    print("总共有[%d]个文件，[%d]个目录" % (i, j))
    print("三不沾[%d]" % t)
    print('---------------------------------------------------')
    
    