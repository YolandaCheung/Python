# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from lxml import etree
import re
import random
import time
import json
from openpyxl import Workbook
from openpyxl import load_workbook
import xlwt
import datetime 

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
    {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
    {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]
    
page=1
url_list=[]
for page in range(1,10):
    urls='http://search.ccgp.gov.cn/bxsearch?searchtype=2'+'&page_index='+str(page)+'&bidSort=0&buyerName=&projectId=&pinMu=0&bidType=0&dbselect=bidx&kw=%E5%A5%87%E8%99%8E360&start_time=2015%3A01%3A01&end_time=2015%3A12%3A31&timeType=6&displayZone=&zoneId=&pppStatus=0&agentName='    
    url_list.append(urls)
print (url_list)
buyer=[]
pn=[]
pu=[]
pc=[]
c=[]
b=[]
for url in url_list:
    req = requests.get(url,headers=hds[random.randint(0,len(hds)-1)]).text
    soup = BeautifulSoup(url,'lxml')
    selector = etree.HTML(req)
    project_name= selector.xpath('/html/body/div[5]/div[2]/div/div/div[1]/ul/li/a/text()[1]')
    project_url=selector.xpath('/html/body/div[5]/div[2]/div/div/div[1]/ul/li/a/@href')
    project_content=selector.xpath('/html/body/div[5]/div[2]/div/div/div[1]/ul/li/p/text()')
    city=selector.xpath('/html/body/div[5]/div[2]/div/div/div[1]/ul/li/span/a/text()')
    buyer=selector.xpath('/html/body/div[5]/div[2]/div/div/div[1]/ul/li/span/text()[1]')
    pn.append(project_name)
    pu.append(project_url)
    pc.append(project_content)
    c.append(city)
    b.append(buyer)
print (pn)
print (pu)
print (pc)
print (c)
print (b)

wb = xlwt.Workbook()
file_name = '奇虎3603.xlsx'
ws = wb.add_sheet('2015',cell_overwrite_ok=True) 
headData = ['项目名称','网址','详情','城市','采购者']#表头部信息
wb.save(file_name)
for colnum in range(0, 4):
    ws.write(0, colnum, headData[colnum], xlwt.easyxf('font: bold on'))  # 行，列
pn3=[]
pu3=[]
pc3=[]
c3=[]
b3=[]
for pn1 in pn:
    for pn2 in pn1:
        pn3.append(pn2)

for pu1 in pu:
    for pu2 in pu1:
        pu3.append(pu2)

for pc1 in pc:
    for pc2 in pc1:
        pc3.append(pc2)

for c1 in c:
    for c2 in c1:
        c3.append(c2)

for b1 in b:
    for b2 in b1:
        b3.append(b2)
i=1        
for i in range(1,len(pn3)):
    ws.write(i,0,pn3[i-1])
    ws.write(i,1,pu3[i-1])
    ws.write(i,2,pc3[i-1])
    ws.write(i,3,c3[i-1])
    ws.write(i,4,b3[i-1])
    i=i+1
wb.save(file_name)