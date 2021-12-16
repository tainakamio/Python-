# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:13:03 2020

@author: Administrator
"""
#p19 修改字符串大小写，方法title，upper，lower
name="ada lavelace"
print(name.title())
name='Ada Lovelace'
print(name.upper())
print(name.lower())

#p21 换行符与制表符
print('languages:\n\tPython\n\tC\n\tJava')

#p21 删除字符串空白
lgg ='python '
print(lgg.strip())
    #这种删除是暂时的
    #strip删除两端的空白；lstrip删除开头空白；rstrip删除末尾空白

#python之禅
import this


#p88 字典.items()遍历字典所有键值对
user = {'first':'enrico','last':'fermi'}
items = user.items()
print(items)
for k,v in items:
    print(k,'\n',v,'\n')


#p130 星号创建空元组，传递任意数量的实参
def make_pizza(*toppings):
    print(toppings)
make_pizza('mushrooms','green peppers','extra cheese')

#p132 两个星号创建空字典，传递任意数量的关键字实参
def build_profie(first, last,**userinfo):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k,v in userinfo.items():
        profile[k] = v
    return profile
user_profile = build_profie('albert','einstein',location = 'princeton', field = 'physics')
print(user_profile)