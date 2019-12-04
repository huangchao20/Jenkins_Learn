import os
import hashlib

def getlistdir(path):
    try:  # 如果path是一个文件的完整名称，os.listdir会抛出错误
        fl = os.listdir(path)
    except Exception as e:
        fl = []
    finally:
        return fl


def getallfile(path):
    allfile = []
    fl = getlistdir(path)
    if len(fl) != 0:
        fl = list(map(lambda x: path + '\\' + x, fl))
        #fl = list(map(lambda x: os.path.join(path, x), fl))
        allfile = allfile + fl
        for f in fl:
            allfile = allfile + getallfile(f)
    return allfile


def makemd5(stri):
    md5 = hashlib.md5()
    md5.update(stri.encode('utf-8'))
    return md5.hexdigest()


def main():
    dirpath = input('需要加密的目录:')
    myfilelist = getallfile(dirpath)  # 获取当前文件'.'中的所有文件和文件夹名list
    myfilestr = '|'.join(myfilelist)  # 文件list转换为以'|'分隔的字符串
    print(myfilestr)  # 显示要进行md5摘要加密的字符
    print("md5=", makemd5(myfilestr))  # 计算并显示md5码

if __name__ == '__main__':
    main()