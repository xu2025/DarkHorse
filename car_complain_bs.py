# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:15:59 2021

@author: 53180
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_page_content(request_url):
    # 获取页面的内容
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html = requests.get(request_url, headers=headers, timeout=20)
    content = html.text
    #print(content)
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup
    
#分析当前页面的投诉信息
def analysis(soup):
    # df用于暂存单页的投诉信息
    df = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
    temp = soup.find('div', class_='tslb_b')
    # 寻找网页中所有类别为tslb_b的行
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        td_list = tr.find_all('td')
        #如果没有td，就是表头th
        if len(td_list) > 0:
            # 投诉编号 投诉品牌 投诉车系 投诉车型 问题简述 典型问题 投诉时间 投诉状态
            id, brand, car_model, type, desc, problem, datetime, status = \
                td_list[0].text,  td_list[1].text,  td_list[2].text,  td_list[3].text, \
                td_list[4].text,  td_list[5].text,  td_list[6].text,  td_list[7].text,
            #print(id, brand, car_model, type, desc, problem, datetime, status)
            temp = {}
            temp['id'] = id
            temp['brand'] = brand
            temp['car_model'] = car_model
            temp['type'] = type
            temp['desc'] = desc
            temp['problem'] = problem
            temp['datetime'] = datetime
            temp['status'] = status
            df = df.append(temp, ignore_index = True)
    return df

result = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
# 请求URL
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
page_num = 20
for i in range(page_num):
    # 拼接当前的url
    request_url = base_url + str(i+1) + '.shtml'
    # 得到soup解析
    soup = get_page_content(request_url)
    # 通过soup解析，得到当前页面的dataframe
    df = analysis(soup)
    result = result.append(df)
    
print(result)
result.to_csv('car_complain.csv', index = False)
result.to_excel('car_complain.xlsx', index = False)