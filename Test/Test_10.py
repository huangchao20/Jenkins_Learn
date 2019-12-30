import requests
from bs4 import BeautifulSoup

url = 'https://news.sina.com.cn/china/'
res = requests.get(url)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.select('div.main-content div.right-content li a'))
# print(soup.select('div.main-content div.left-content-1 h2'))
tag = soup.li
print(tag)
print(tag.name)
# print(soup.prettify())
# print(soup.select('li a'))
# print(soup == soup.prettify())