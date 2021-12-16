# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:50:40 2020

@author: Administrator
"""


#第十章——文件和异常
#目次
#open,read,readlines,write,try-except

#读取——read
with open('D:\\The 7th Art\\books\\pi_digits.txt') as file:
    contents = file.read()
    print(contents)

#逐行读取——for循环
with open('D:\\The 7th Art\\books\\pi_digits.txt') as file:
    for line in file:
        print(line)

#逐行读取——readlines
with open('D:\\The 7th Art\\books\\pi_digits.txt') as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line)
        
#使用文件内容
with open('D:\\The 7th Art\\books\\pi_digits.txt') as file:
    lines = file.readlines()
    pi_string = ''
    for line in lines:        
        pi_string += line.strip()
    print(pi_string)


# open()的实参：r，w，a，r+
# r——只读
# w——写入
# a——附加
# r+——读取和写入
    
#写入文件——w
filename = 'abc.txt'
with open(filename,'w') as file_obj:
    file_obj.write('abc')
#附加——a，这样的话不会覆盖原有内容
filename = 'abc.txt'
with open(filename,'a') as file_obj:
    file_obj.write('def')

#try-except代码块处理异常
try:
    print(5/0)
except ZeroDivisionError:
    print('不能用0除')

    




