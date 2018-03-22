#-*- coding:utf-8 -*-

import json
import requests
import xlwt
import time
from lxml import etree


#获取存储职位信息的json对象，遍历获得公司名、福利待遇、工作地点、学历要求、工作类型、发布时间、职位名称、薪资、工作年限
def get_json(url,datas):

    my_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput='
    }
    cookies = {
        'Cookie': 'user_trace_token=20171023210242-74b36b68-b7f2-11e7-960c-5254005c3644; LGUID=20171023210242-74b373b3-b7f2-11e7-960c-5254005c3644; index_location_city=%E6%B7%B1%E5%9C%B3; JSESSIONID=ABAAABAACEBACDG60417EF8F931F7B52216D331C5A46D68; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=search_code; _gat=1; LGSID=20171102222506-9f55d9b8-bfd9-11e7-b429-525400f775ce; LGRID=20171102223926-a01bd03e-bfdb-11e7-b449-525400f775ce; _ga=GA1.2.1716241772.1508763746; _gid=GA1.2.1172760451.1509632661; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508763746,1509632661; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1509633545; SEARCH_ID=25e90fb37fa44438a176d88b2b0f89bc'
    }
    time.sleep(30)
    content = requests.post(url=url,cookies=cookies,headers=my_headers,data=datas)
    # content.encoding = 'utf-8'
    result = content.json()
    print (result)
    info = result['content']['positionResult']['result']
    print (info)
    info_list = []
    for job in info:
        information = []
        information.append(job['positionId']) #岗位对应ID
        information.append(job['companyFullName']) #公司全名
        information.append(job['companyLabelList']) #福利待遇
        information.append(job['education']) #学历要求
        information.append(job['firstType']) #工作类型
        information.append(job['formatCreateTime']) #发布时间
        information.append(job['positionName']) #职位名称
        information.append(job['salary']) #薪资
        information.append(job['workYear']) #工作年限
        information.append(job['industryField'])#行业
        information.append(job['financeStage'])#融资情况
        information.append(job['companySize'])#公司规模
        information.append(job['positionLables'])#职位标签
        info_list.append(information)
        #将列表对象进行json格式的编码转换,其中indent参数设置缩进值为2
        print (json.dumps(info_list,ensure_ascii=False,indent=2))
        print (info_list)
    return info_list

def main():     
    info_result = []
    title = ['岗位id','公司全名','福利待遇','学历要求','工作类型','发布时间','职位名称','薪资','工作年限','行业','融资情况','公司规模','职位标签']
    info_result.append(title)
    x=1
    for x in range(1,3):
        url='https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0'
        datas = {
            'first': True,
            'pn': x,
            'kd': '数据分析'
        }
        info = get_json(url,datas)
        info_result = info_result+info
        wb=workbook()
        ws1=wb.active
        ws1.title = '数据分析'
        for row in info_result:
            ws1.append(row)
        wb.save('analyst.xls')


if __name__ == '__main__':
    main()      