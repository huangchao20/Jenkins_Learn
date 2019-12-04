import requests
import json


class Doubanspider:

    def __init__(self):
      #要将callback去掉，url地址是在network中含有信息的包的url地址
      #可以用ctrl+f的快捷键在network页面查找
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=0"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
            "Referer": "https: // m.douban.com / tv / american"}
            #headers要带referer，因为是手机版，不要会报错
    def run(self):  # 实现主要逻辑

        num = 0
        total = 100
        while num < total + 18:
            start_url = self.temp_url.format(num)
            response = requests.get(url=start_url, headers=self.headers)
            html_str = response.content.decode()
            print(type(html_str))
            content_list, total = self.get_content_list(html_str)
            self.save_content_list(content_list)
            num += 18

    def get_content_list(self, html_str):
        dict_data = json.loads(html_str)
        content_list = dict_data["subject_collection_items"]
        total = dict_data["total"]
        return content_list, total

    def save_content_list(self, content_list):
      #a代表可追加模式
        with open("douban.json", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")

        print("save succeed")


if __name__ == '__main__':
    douban = Doubanspider()
    douban.run()