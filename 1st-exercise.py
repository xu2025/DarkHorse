# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:30:20 2021

@author: mowmow
"""
#Action1: 求2+4+6+8+...+100的求和，用Python该如何写？
#%%
#for循环
sum = 0

for number in range(1,101):
    if number % 2 == 0:
        sum = sum + number
        
    number = number + 1
print("The result of for-loop is",sum)

#%%
#while循环
sum = 0
number = 2

while number< 101:
    sum = sum + number
    number = number + 2
    
print("The result of while-loop is",sum)

#Action2: 统计全班的成绩，班里有5名同学，现在需要你用Python来统计下这些人
#在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
#然后把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）
#%%
from pandas import Series, DataFrame
import numpy as np
data = {'Chinese': [68, 95, 98, 90, 80], 
        'Math': [65, 76, 86, 88, 90], 
        'English': [30, 98, 88, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, 
                index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], 
                columns=['Chinese', 'Math', 'English'])

#print(df2) 
#计算语文数学英语的平均成绩、最小/大成绩、标准差
print(df2.describe())
#计算语文数学英语的方差
print(df2.std())    
#计算总成绩Score
df2['Score']=df2.apply(lambda x: x.sum(),axis=1)
#得到名词，并输出成绩
df2 = df2.sort_values('Score',ascending=False).reset_index()
print(df2)

#Action3:Step1，数据加载
#Step2，数据预处理：拆分problem类型 => 多个字段
#Step3，数据统计
#对数据进行探索：
#①品牌投诉总数，
#②车型投诉总数
#③哪个品牌的平均车型投诉最多
#%%
import pandas as pd

#数据加载
df = pd.read_csv('./car_complain.csv')
#print(df)
#df.to_excel('./car_complain.xlsx',index=False)

df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))
#print(df)

#数据清洗,将别名合并
def f(x):
    x = x.replace('一汽-大众','一汽大众')
    return x
df['brand'] = df['brand'].apply(f)
#数据统计
#①品牌投诉总数
result1 = df.groupby(['brand'])['id'].agg(['count'])
result1 = result1.sort_values('count',ascending=False)
print(result1)
#②车型投诉总数
result2 = df.groupby(['car_model'])['id'].agg(['count'])
result2 = result2.sort_values('count',ascending=False)
print(result2)
#③哪个品牌的平均车型投诉最多
result3 = df.groupby(['brand','car_model'])['id'].agg(['count'])
result3 = result3.sort_values('count',ascending=False)
print(result3)
