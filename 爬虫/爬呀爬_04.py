import requests
import re

url = 'http://www.17k.com/list/2932117.html'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
"""
<h1 class="Title">九龙拉棺</h1>
"""
title = re.findall(r'<h1\sclass="Title">(.*?)</h1>', html)[0]
#title = re.findall(r'<h1 class="Title">(.*?)</h1', html)[0]

fb = open('%s.txt' % title, 'w', encoding='utf-8')
dl = re.findall(r'dl\sclass="Volume">.*?</dl>', html, re.S)[0]
# dd = re.findall(r'<dd>.*?</dd>', dl, re.S)
dd = re.findall(r'<dd>.*?</dd>', dl, re.S)[0]
# print(dd.strip())
"""
<a target="_blank" href="/chapter/2932117/36746487.html" title="第二章 骑龙穴字数：3086更新日期:2019-01-01 20:01:27">
	<span class="ellipsis ">第二章 骑龙穴</span>
</a>
"""
fd = open("dd.txt", 'w', encoding='utf-8')


dd = dd.replace('\n', '').replace('\t', '')
fd.write(dd)
# chapter_info_list = re.findall(r'href="(.*?)".*?>\n.*?<span class="ellipsis.*?">\n\s{60}(.*?)\n\s{52}<', dd)
# chapter_info_list = re.findall(r'href="(.*?)".*?\n\s<span class="ellipsis vip">(.*?)</span>', dd)
#chapter_info_list = re.findall(r'href="(.*?)".*?<span class="ellipsis.*?">(.*?).*?</span>', dd)
chapter_info_list = re.findall(r'href="(.*?)".*?<span class="ellipsis .*?">(.*?)</span>', dd)

for cil in chapter_info_list:
    chapter_url, chapter_tittle = cil
    chapter_url ="http://www.17k.com%s" % chapter_url
    print(chapter_url)
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'utf-8'
    chapter_html = chapter_response.text
    chapter_html = chapter_html.replace('\n', '').replace('\t', '')
    # print(chapter_html)
    chapter_content = re.findall(r'<div class="p">(.*?)<p class="copy.*?">', chapter_html, re.S)[0]
    
    
    # chapter_content = re.findall(r'<div class="p">(.*?)<div class="author-say"></div>', chapter_html, re.S)[0]
    chapter_content = chapter_content.replace(' ', '')
    chapter_content = chapter_content.replace('&#12288;', '')
    chapter_content = chapter_content.replace('<br/>', '')
    chapter_content = chapter_content.replace('<p>', '    ').replace('</p>', '\n')
    # chapter_content = chapter_content.replace('</p>', '\n')
    # print(chapter_content)

    fb.write(chapter_tittle)
    fb.write(chapter_content)
    fb.write('\n*5')
    
