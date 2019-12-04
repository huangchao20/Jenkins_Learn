import requests

# session = requests.session()
# url = "http://www.renren.com/PLogin.do"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36"}
# date = {
#     "email": "15869117206",
#     "password": "a588181"
# }
#
# ttt = session.post(url, headers=headers, data=date)
# print(ttt)
# url1 = "http://www.renren.com/966470757/profile"
# sss = session.get(url1)
# print(sss)

import json

class DoubanSpider:
    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=0"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
            "Referer": "https: // m.douban.com / tv / american"}
    
    def run(self):
        num = 0
        total = 100
        while num < total + 18:
            start_url = self.temp_url.format(num)
            response = requests.get(url=start_url, headers=self.headers)
            html_str = response.content.decode()
            content_list, total = self.get_content_list(html_str)
            self.save_content_list(content_list)
            num += 18
    
    def get_content_list(self, html_str):
        dict_data = json.loads(html_str)
        print(dict_data)
        content_list = dict_data['subject_collection']
        total = dict_data['total']
        return content_list, total
    
    def sava_content_list(self, content_list):
        with open('douban.json', 'a', encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write('\n')
        print('write Succeed')

if __name__ == '__main__':
    douban = DoubanSpider()
    douban.run()