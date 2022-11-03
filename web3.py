#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:02:29 2022

@author: leopeng
"""
import requests
from lxml import etree
import numpy as np
import pandas as pd
import csv
import xlwt
#设置环境

urls = []
#获取所有网页
for i in range(1,21,1):
    i = i * 1
    url = "https://web3.career/intern-jobs?page={}".format(i)
    urls.append(url)




headers = {"User-Agent":
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

#detail_urls= []
#for url in urls:
    #发送请求
    #response = requests.get(url,headers = headers)
    #编码转码
    #content = response.content.decode("utf8")
    #解析html字符串
    #html = etree.HTML(content)
    #xpath提取每个职位的URL
   # detail_url = html.xpath('//header/div[1]/div[1]/a/@href')
    #detail_urls.append(detail_url)
   # print(detail_url)
   # break
                       

internship = []
i = 1

def get_info(url): #for page in detail_urls:
     for url in urls:
                try:

                #发送请求
                    response = requests.get(url,headers = headers)#编码转码
                    content = response.content.decode("utf8")
                    html = etree.HTML(content)
                #抓取职位名称
                    title = html.xpath('//div/div/div/a/h2/text()')[0]
                    print(title)
                #公司名
                    company = html.xpath('//div/a/h3/text()')[0]
                    print(company)
                #地点
                    location = html.xpath('//td[2]/a[1]/text()')[1]
                    print(location)
                #薪资
                    salary = html.xpath('//div/p[@title ="Estimated salary based on similar jobs"]/text()')[2]
                    print(salary)



                    internship = {
                        "title":title,
                        "company":company,
                        "location":location,
                        "salary":salary,
                    }
                    internship.append(internship)
                    print(internship)


                except:
                    continue

if __name__ == '__main__':
    urls = ['https://web3.career/intern-jobs?page={}'.format(str(i)) for i in range(1,21,1)]

    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet1')
    header = ['title', 'company', 'location', 'salary']
    for h in range(len(header)):
        sheet.write(0, h, header[h])
    count = 1
    i = 1
    for url in urls:
        get_info(url)
        print('Page' + str(count) + "Done")
        count += 1
    for list in internship:
        j = 0
        for internship in list:
            sheet.write(i, j, internship)
            j += 1
        i += 1

    book.save('/Users/leopeng/Desktop/5507 Data/web3.xls')


#import csv
#keys=list(internship[0].key())
#headers = list(internship[0].key())

#with open(r"/Users/leopeng/Desktop/5507 Data/web3.csv","w", newline="") as f:
            #writer = csv.DictWriter(f,headers,delimiter='|')
            #writer.writeheader()
           # for data in internship:
               # writer.writerows(internship)

#i += 1 # i=i+1
#print("第{}页已经爬取完毕".format(i))
