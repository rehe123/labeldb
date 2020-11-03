import os
import requests
from lxml import etree


# http://tieba.baidu.com/f?kw=%E7%BE%8E%E9%A3%9F&ie=utf-8&pn=50


class TiebaSpider:
    def __init__(self):
        self.proxies = {"proxies": "http:116.54.3.229:45068"}
        self.base_url = "http://tieba.baidu.com/f?"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    def send_request(self, url):
        html = requests.get(url, proxies=self.proxies, headers=self.headers)
        return html.content

    def extract_tiezi_url(self, tieba_html):
        html_obj = etree.HTML(tieba_html)
        urls = html_obj.xpath("//a[@class='j_th_tit ']/@href")
        return ["http://tieba.baidu.com" + path for path in urls]

    def extract_img_url(self, tiezi_html):
        html_obj = etree.HTML(tiezi_html)
        urls = html_obj.xpath("//img[@class='BDE_Image']/@src")
        return urls

    def write_file(self, file_content, file_name):
        with open(file_name, "wb") as f:
            print("正在保存 %s..." % file_name)
            f.write(file_content)

    def start(self, tieba_name, page_count):
        os.mkdir(tieba_name)
        # 拼接url
        for page in range(1, page_count + 1):
            query_str = "kw=%s&ie=utf-8&pn=%d" % (tieba_name, (page - 1) * 50)
            tieba_url = self.base_url + query_str
            # 请求贴吧url
            tieba_html = self.send_request(tieba_url).decode("utf-8")
            # 提取帖子url
            tiezi_urls = self.extract_tiezi_url(tieba_html)
            # 请求帖子url
            for tiezi_url in tiezi_urls:
                tiezi_html = self.send_request(tiezi_url).decode("utf-8")
                # 提取图片url
                img_urls = self.extract_img_url(tiezi_html)
                # 请求图片url
                for img_url in img_urls:
                    img_bytes = self.send_request(img_url)
                    # 保存文件
                    self.write_file(img_bytes, "./{}/".format(tieba_name) + img_url[-10:])


if __name__ == '__main__':
    tieba_n = input("请输入贴吧名:")
    page_c = int(input("请输入爬取页数:"))
    spider = TiebaSpider()
    spider.start(tieba_n, page_c)
