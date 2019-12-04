import re
from bs4 import BeautifulSoup
from urllib import request
import requests

# url = 'https://list.jd.com/list.html?cat=12379,12380'
# rqs = request.urlopen(url)
# with open('G:\\黄大宝python\\测试目录\\爬虫文件\\spider01', 'w+') as fs:
#     fs.write(rqs.read().decode("utf-8"))

# url = 'https://you.163.com/item/list?categoryId=1010000&subCategoryId=1008003'
# res = requests.get(url).text
# # print(res)
# # <span data-reactid=".3.1.1.$1008003.1.$3810010.0.4.2.1.1">419</span>
# content = BeautifulSoup(res, "html.parser")
# ul = content.find_all('img class')
# print(len(ul))

url = 'https://www.zhipin.com/job_detail/?query=python&city=101010100'

res = requests.get(url).text
# print(res)
content = BeautifulSoup(res, "html.parser")
ul = content.find_all('ul')
print(len(ul))