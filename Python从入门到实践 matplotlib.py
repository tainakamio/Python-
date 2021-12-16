# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 13:39:54 2020

@author: Administrator
"""
#第十五章
#目次
#plot,title,fontsize,xlabel,ylabel,tick_params，savefig，cmap
#随机漫步
#利用Pygal画矢量图


import matplotlib.pyplot as plt
import numpy as np

#绘制折线图
squares = [1,4,9,16,25]
plt.plot(squares)
plt.show()

#图表标题、轴标题、轴刻度、字号、线粗
squares = [1,4,9,16,25]
plt.plot(squares,linewidth=5) #线粗
plt.title('Square Numbers',fontsize=24) #图表标题
plt.xlabel('Values',fontsize=14) #坐标轴标题
plt.ylabel('Square of Values',fontsize=14)
plt.tick_params(axis='both',labelsize=14) 
#tick_params指定刻度样式，axis指定应用于哪个轴，labelsize是刻度标记的字号
plt.show()


#指定x轴与y轴的一一对应
squares = [1,4,9,16,25]
input_squares = [1,2,3,4,5]
plt.plot(input_squares,squares)
plt.show()
plt.savefig('squares_plot.png',bbox_inches='tight')
#储存图片，指定文件名。bbox_inches='tight'表示除去空白，若想保留则不用。


#自动计算并绘制散点图
x = list(range(1,1001)) 
y = [i**2 for i in x]
#如果写y = (i**2 for i in x),会报错。你妈的，为什么？
plt.scatter(x,y,s=40) #s表示点的尺寸
plt.axis([0,1100,0,1100000])
#也可以写plt.axis('auto')，能自动匹配坐标轴长度
#写plt.axis(0,1100,0,1100000)，会报错，但还是能跑出图像来
plt.show()



#自定义颜色
squares = [1,4,9,16,25]
input_squares = [1,2,3,4,5]
plt.scatter(input_squares,squares,c='green',edgecolor='none',s=40)
#edgecolor是点的轮廓颜色，默认为黑。令其=none意味着删除轮廓色。
plt.show()
#除此以外还可用RGB分量指定颜色，如c=(10,11,12)

#使用颜色映射——cmap
x = list(range(1,1001)) 
y = [i**2 for i in x]
plt.scatter(x,y,c=y,cmap=plt.cm.Blues,edgecolor='none',s=40)
plt.show()


#随机漫步
from random import  choice

class Randomwalk():
    def __init__(self,num_points=5000):
        self.num_points = num_points
        self.xvalue=[0]
        self.yvalue=[0]
        
    def fill_walk(self):
        while len(self.xvalue)<self.num_points:
            
            xdirection=choice([-1,1])
            xdistance=choice([0,1,2,3,4])
            xstep=xdirection*xdistance
            ydirection=choice([-1,1])
            ydistance=choice([0,1,2,3,4])
            ystep=ydirection*ydistance
            
            next_x = self.xvalue[-1]+xstep
            next_y = self.yvalue[-1]+ystep
            
            self.xvalue.append(next_x)
            self.yvalue.append(next_y)

rw = Randomwalk()
rw.fill_walk()
plt.scatter(rw.xvalue,rw.yvalue,c=rw.yvalue,cmap=plt.cm.Blues,s=1)
plt.show()


 #多次随机漫步
while True:
    rw = Randomwalk()
    rw.fill_walk()
    plt.scatter(0,0,c='yellow',s=100) #突出起点
    plt.scatter(rw.xvalue[-1],rw.yvalue[-1],c='green',s=100) #突出终点
    plt.scatter(rw.xvalue,rw.yvalue,c=rw.yvalue,cmap=plt.cm.Blues,s=1)
    #将坐标轴设为不可见
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.show()
    
    keep_running = input('make another randomwalk?(y/n):')
    if keep_running == 'n':
        break
    
    
#
from random import randint

class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1,self.num_sides)


#模拟一个骰子，并计算频数
die = Die()  
results = []
freqs = []
for i in range(100):
    result = die.roll()
    results.append(result)
print(results)
for v in range(1,die.num_sides+1):
    freq = results.count(v)
    freqs.append(freq)
print(freqs)

#为骰子绘制矢量图
import pygal #似乎没安装此模块
hist = pygal.Bar()
hist.xlabels = ['1','2','3','4','5','6']
hist.add('D6',freqs)
hist.render_to_file('die_visual.svg')

#思考：同时掷n个m面骰子k次，写成函数f(n,m,k),并绘制矢量图


    
                            







