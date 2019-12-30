import requests
from bs4 import BeautifulSoup
import json
import time
import os

def get_web_info(who_sells):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9 '
    }
    url = 'http://bj.58.com/pbdn/pn{}/'.format(who_sells)
    print('url:', url)
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    print(soup.select('td.t  a.t'))
    # return soup.select('td.t  a.t')

def createFile(dpat, who_sells):
    if not os.path.isdir(dpat):
        os.mkdir(dpat)
    filename = os.path.join(dpat, dpat.split('\\').pop() + str(who_sells) + ".txt")
    return filename

if __name__ == '__main__':
    dpat = 'G:\\黄大宝python\\测试目录\\爬你妈背时\\'
    # for who_sells in range(1, 5):
    #     get_web_info(who_sells)
        # filename = createFile(dpat, who_sells)
        # with open(filename, 'w+') as fs:
        #     for ws in get_web_info(who_sells):
        #         fs.write((str(ws)))
    get_web_info(1)