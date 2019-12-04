import urllib.request
import json

def GetJsonData(url):
    data = urllib.request.Request(url)
    print(type(data))
    # jsData = json.load(data)
    # print(jsData)
    
if __name__ == '__main__':
    url = 'https://home.firefoxchina.cn/'
    GetJsonData(url)