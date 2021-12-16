# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:46:58 2020

@author: Administrator
"""


import csv


#读取csv文件头
fn = 'D:\\The 7th Art\\books\\sitka_weather_2018_full.csv'

with open(fn) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

#打印文件头及其位置
with open(fn) as f:
     reader = csv.reader(f)
     header_row = next(reader)
     for index,column in enumerate(header_row):
         print(index,column)


with open(fn) as f:
    reader = csv.reader(f)
    header_row = next(reader) #先把头行（都是变量名）读掉，这样才能从第二行开始
    highs= []
    for row in reader:  #如上所述，从第二行开始读
        highs.append(int(row[8])) 
    print(highs)

#绘制最高温曲线图

import matplotlib.pyplot as plt

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(highs,c='red')
plt.title('Daily high temperatures',fontsize=16)
plt.xlabel('',fontsize=16)
plt.ylabel('Temperature',fontsize=16)
plt.tick_params(axis='both',labelsize=16)
plt.show()


#绘制最高温曲线图，并附带日期

from datetime import  datetime

with open(fn) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates = []
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        #然而这里是/分割的，书上的数据是-分割的，用不了strptime
        dates.append(current_date)

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.title('Daily high temperatures',fontsize=16)
plt.xlabel('',fontsize=16)
plt.ylabel('Temperature',fontsize=16)
plt.tick_params(axis='both',labelsize=16)
plt.show()


#使用try-except-else代码块处理数据缺失问题


