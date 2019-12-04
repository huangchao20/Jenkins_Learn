import os

def test(filename):
    with open(filename, 'r', encoding='GBK') as fs:
        # print(fs.readlines())
        lines = list(fs)
        sp = '"$inputCtx" = "Y" -a ! "$inputCtx" = "y"'
        # for fr in lines:
        #     if fr.startswith('read -p'):
        # print(lines)
        frs = list(fr for fr in range(len(lines)) if 'read' in lines[fr])
        
        # for fr in lines:
        #     if 'read -p' in fr:
        #         print(fr)
        
if __name__ == '__main__':
    filename = 'G:\\黄大宝python\\2019\\20191024\\特色业务平台\\fbap.20191024r.t11\\XQ-2019-502\\TS_82823_X_20191024.sh'
    test(filename)