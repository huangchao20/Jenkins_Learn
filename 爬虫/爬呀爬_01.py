import urllib.request
import json
import requests
import os

path = 'G:\\黄大宝python\\测试目录\\爬虫文件\\'
id = '2374240301'
proxy_addr = "122.241.72.191:808"        #代理IP
pic_num = 0
weibo_name = 'programmer'
url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id

def use_proxy():
    req = urllib.request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    return data
    
def get_User_Info():
    data = use_proxy().encode('utf-8')
    content = json.loads(data).get('data')
    print(type(content))
    print(content.get('userInfo').get('id'))
    print(content['userInfo']['id'])
    
if __name__ == "__main__":
    get_User_Info()