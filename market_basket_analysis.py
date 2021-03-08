# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 09:49:54 2021

@author: Xu haojie-PFEM
"""

# ToDo：统计交易中的频繁项集和关联规则
# 思路：1. 遍历所有数据，去除所有空值
# 2. 挖掘数据


import pandas as pd

pd.set_option('max_columns', None)
# 数据加载
raw_data = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)
print(raw_data.shape)   # 查看数据形状
print(raw_data.head())  # 查看头部数据

transactions = []
# 按照行进行遍历
for i in range(0, raw_data.shape[0]):
    # 记录一行Transaction
    temp = []
    # 按照列进行遍历
    for j in range(0, raw_data.shape[1]):
        if str(raw_data.values[i ,j]) != 'nan': 
            temp.append(raw_data.values[i, j])
    #print(temp)
    transactions.append(temp)

from efficient_apriori import apriori
itemsets, rules = apriori(transactions, min_support=0.02, min_confidence=0.4)
print('频繁项集:', itemsets)
print('关联规则:', rules)