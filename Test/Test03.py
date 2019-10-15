import os

print("Hello 1")
print(333333333333333333333)


def printFile(filename):
    if os.path.isfile(filename):
        with open(filename) as fs:
            print(fs.readlines())
    elif os.path.isdir(filename):
        print(os.listdir())
    else:
        print('~~~调皮~~~')

if __name__ == '__main__':
    filenames = ['123888', 'G:\\黄大宝python\\2018\\20181018\\特色业务平台\\特色业务平台.20181018r.t2\\workspace\\PyTrade_fbap\\TBATCH_Proc_File_CK_EndStat.py', 'G:\\黄大宝python\\2018', 'G:\\黄大宝python\\2018\\20181018\\特色业务平台\\特色业务平台.20181018r.t2\\workspace\\PyTrade_fbap\\TBATCH_Proc_File_CK_EndStat.py']
    for filename in filenames:
        printFile(filename)