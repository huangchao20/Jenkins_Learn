import requests
from bs4 import BeautifulSoup
import time
import datetime
import os

def getNews():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9 '
    }
    url = 'http://news.sina.com.cn/china/'
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'html.parser')
    # fda = soup.findall(class_='right_content')
    # fda = soup.select('div.main-content div.path-search div.path')
    fda = soup.select('#feed_cont')
    print(fda)
    # print(type(fda))

def createNewsFile():
    baseDir = 'G:\\黄大宝python\\测试目录'
    today = str(datetime.date.today()).replace('-', '')
    NewsDir = os.path.join(baseDir, today)
    if not os.path.isdir(NewsDir):
        os.mkdir(NewsDir)
    
    
if __name__ == '__main__':
    getNews()