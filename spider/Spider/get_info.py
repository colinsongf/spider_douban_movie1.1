# -*- coding: utf-8 -*-
from save_to_excel import *
import urllib2
from lxml import etree
import urllib
import time


def get_info(dirs, tags):
    for tag in tags:
        page_num = 0
        excel_row = 0

        while page_num < 10000:
            url = "http://www.douban.com/tag/" + tag + '/movie?start=' + str(page_num)  # page_num 每次递加15
            page_num += 15

            try:
                request = urllib2.Request(url.encode('utf-8'), headers={
                'Connection': 'keep-alive',
                'Accept': 'image/webp,image/*,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
                'Referer': url.encode('utf-8')
            })
                response = urllib2.urlopen(request)
                content = response.read().decode('utf-8')
                html_content = etree.HTML(content)

                for row in range(1, 15):  # 每页有15个，遍历15个电影
                    path = '//*[@id="content"]/div/div[1]/div[1]/dl[' + str(row) + ']/dd/a/@href'
                    movie_url = html_content.xpath(path)  # 从当前页获取电影相应的url
                    if movie_url:
                        time.sleep(5)
                        request2 = urllib2.Request(movie_url[0], headers={
                'Connection': 'keep-alive',
                'Accept': 'image/webp,image/*,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
                'Referer': movie_url[0]
            })  # 访问电影的url 获取评分和人数等信息
                        response2 = urllib2.urlopen(request2)
                        content2 = response2.read().decode('utf-8')
                        html_content2 = etree.HTML(content2)
                        # 定位元素
                        movie_name_path = '//*[@id="content"]/h1/span[1]/text()'
                        rate_path = '//*[@id="interest_sectl"]/div/div[2]/strong/text()'
                        people_num_path = '//*[@id="interest_sectl"]/div/div[2]/div/div[2]/a/span/text()'
                        # 获取信息
                        movie_name = html_content2.xpath(movie_name_path)
                        rate = html_content2.xpath(rate_path)
                        people_num = html_content2.xpath(people_num_path)

                        # 如果评论人数大于2w,评分大于7 则保存到Excel中
                        if movie_name and rate and people_num:  # list不为空
                            if int(people_num[0]) > 20000 and float(rate[0]) > 7:
                                excel_row += 1
                                save_to_excel(dirs, tag, excel_row, movie_name[0], rate[0], people_num[0], movie_url[0])

                        else:
                            print("not found the infomation")

                    else:
                        page_num = 10000
                        print("no movie url,turn to next tag")
                        break

            except urllib2.HTTPError, e:
                print e.code
            except urllib2.URLError, e:
                print e.reason

        print("%s movies has all saved" % tag)
    print("all mission success")