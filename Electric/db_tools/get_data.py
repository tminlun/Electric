# _*_ encoding:utf-8 _*_
__date__: '2019/11/10 0010 22:11'

 # 把django的models独立使用，用来导入数据（除了能在views使用，还能在别的py文件使用）
import sys
import os

# 获取当前文件的路径 （运行脚本）
pwd = os.path.dirname(os.path.realpath(__file__))
# 获取项目名的全部目录【db_tools】(因为我的当前文件是在项目名下的文件夹下的文件.所以是../
sys.path.append(pwd + "../")

#要想单独使用django的model，必须指定一个环境变量，会去settings配置找（连接数据库）
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Electric.settings")

import django
django.setup()



# 爬取数据
import requests
import time
from lxml import etree
from urllib import request

from company.models import CompanyCategory


class Crawling(object):
    def __init__(self):
        self.index_url = "http://www.tds-1300.com"
        self.about_url = "http://www.tds-1300.com/about/108.html"

    def get_url(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
            "Referer": "http://www.tds-1300.com/about/108.html"
        }
        respone = requests.get(url=url, headers=headers)
        text = respone.text

        return text

    def get_index(self):
        text = self.get_url(self.index_url)
        html = etree.HTML(text)

        # 轮播图
        banners = html.xpath('//ul[@id="slider"]/li/img/@src')
        # 概况
        demo1 = html.xpath('//td[@id="marquePic11"]//td[@align="center"]//img/@src')
        # 企业咨询
        demo2 = html.xpath('//div[@id="demo2"]//td[@align="center"]//img/@src')
        # 企业咨询
        demo3 = html.xpath('//div[@id="demo3"]//td[@align="center"]//img/@src')

        count2 = 1
        count3 = 1


        # 企业咨询
        for marque in demo2:
            time.sleep(0.5)
            marque_url = self.index_url + marque

            # 下载图片
            request.urlretrieve(marque_url, "../static/images/ZX/%s.png" % count2)
            count2 += 1

        # 企业咨询
        for marque in demo3:
            time.sleep(0.5)
            marque_url = self.index_url + marque

            # 下载图片
            request.urlretrieve(marque_url, "../static/images/KJ/%s.png" % count3)
            count3 += 1


        # 概况
        # for marque in demo1:
        #     time.sleep(0.5)
        #     marque_url = self.index_url + marque
        #
        #     # 下载图片
        #     request.urlretrieve(marque_url, "../static/images/GK/%s.png" % count)
        #     count += 1

        '''
        for banner in banners:
            time.sleep(0.5)
            banner_url = "http://www.tds-1300.com" + banner

            # 下载图片
            request.urlretrieve(banner_url, "../static/images/banner/%s.png" % count)
            count += 1
        '''


def main():
    crawling = Crawling()
    crawling.get_index()


if __name__ == '__main__':
    main()


