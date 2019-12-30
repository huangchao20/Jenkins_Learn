# 爬取微信公众号的文章，主要是构造url，而且要准备多个IP
import requests, re, os, random
from lxml import etree
from urllib.parse import urlencode

agents = [
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1"]

proxies = [{'http': 'http://121.43.170.207:3128'}, {'http': 'http://183.56.177.130:808'},
           {'http': 'http://121.42.167.160:3128'}, {'http': 'http://118.190.95.43:9001'}]

proxies = random.choice(proxies)
print('正在使用代理：', proxies)
headers = {'User-Agent': '%s' % random.choice(agents)}
print('正在使用请求头：', headers)


def gethtml(number, index=''):
    params = {
        'type': number,
        'query': index
    }
    url = 'https://weixin.sogou.com/weixin?' + urlencode(params)
    html = requests.get(url, headers=headers, proxies=proxies)
    html.encoding = 'utf-8'
    soup = etree.HTML(html.text)
    if html.status_code == 200:
        print('页面请求成功')
        return soup
    else:
        print('页面无法请求')


def get_articleurl(objects):
    urls = objects.xpath('//ul/li[starts-with(@id,"sogou_vr_11002601_box")]')
    for url in urls:
        arturl = url.xpath('//h3/a/@href')
        for art in arturl:
            art = art.replace('http', 'https')
            print(art)
            yield art


def parse_url(url):
    html = requests.get(url, headers=headers, proxies=proxies)
    html.encoding = 'utf-8'
    soup = etree.HTML(html.text)
    title = soup.xpath('//*[@id="activity-name"]/text()')[0].replace(' ', '')
    contents = soup.xpath("//p/span/text()")
    date = soup.xpath("//div[@id='meta_content']/em[@id='publish_time']/text()")
    print(title, contents, date)


if __name__ == '__main__':
    # for number in range(2,100):
    objects = gethtml(2, 'python')
    art = get_articleurl(objects)
    for ar in art:
        parse_url(ar)
