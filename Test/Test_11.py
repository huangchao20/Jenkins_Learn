import requests
from bs4 import BeautifulSoup

url = 'http://reeoo.com/'
res = requests.get(url)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.select('article.box div#main li#'))
# print(soup.select('div.pagebar'))
# print(soup.title)
tag = soup.article.div.ul.find_all('li')
tag1 = soup.article.div.ul
# print(tag)
# for t in tag:
#     print(t)

# content = tag1.contents
# print(content)

children = tag1.children
# print(children)
# for child in children:
#     print(child)

# print(soup.body.article.div.ul.select('div.thumb'))
# print(soup.find_all(id="list"))
# print(soup.find_all('footer', id='footer'))
# print(soup.find_all('footer') == soup.find_all('footer', id='footer') == soup.find_all(id='footer'))
print(soup.find_all(target=True))
