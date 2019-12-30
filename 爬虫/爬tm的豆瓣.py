import requests
import json

class Douban:
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
            print(start_url)
            response = requests.get(start_url, headers=self.headers)
            html_str = response.content.decode()
            
            continue_list, total = self.get_content_list(html_str)
            self.save_content_list(continue_list)
            
    def get_content_list(self, html):
        dict_data = json.loads(html)
        content_list = dict_data["subject_collection_items"]
        total = dict_data["total"]
        return content_list, total

    def save_content_list(self, content_list):
        # a代表可追加模式
        with open("douban.json", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("save succeed")

if __name__ == '__main__':
    douban = Douban()
    douban.run()