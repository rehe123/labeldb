import os
import requests
import time


class TiebaSpider:
    def __init__(self):
        self.proxies = {"proxies": "http:116.54.3.229:45068"}
        self.base_url = "https://blog.csdn.net/weixin_45651336/article/details/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    def send_request(self, url):
        html = requests.get(url, proxies=self.proxies, headers=self.headers)
        return html.content


if __name__ == '__main__':
    spider_01 = TiebaSpider()

    while True:
        for article in ['109456476'
            , '109456786'
            , '109456872'
            , '109457547'
            , '109458088'
            , '109458239'
            , '109458451'
                        ]:
            url = spider_01.base_url + str(article)
            print(url)
            spider_01.send_request(url)
            time.sleep(3)
