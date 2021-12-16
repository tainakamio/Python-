# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 12:48:58 2020

@author: Administrator
"""
#第三章——列表
#目次
#insert，del，pop，remove，sort，sorted,reverse



#向列表插入元素——insert
tmp = ['a','b','d']
tmp.insert(2,'c')
print(tmp)


#删除：永久删除——del；暂时弹出——pop；按值暂时删除——remove
tmp = ['a', 'b', 'c', 'd']
del tmp[2]
print(tmp)

tmp = ['a', 'b', 'c', 'd']
tmp_pop = tmp.pop() #不填括号的话，默认删除最后一个元素
print(tmp)
print(tmp_pop)

tmp = ['a', 'b', 'c', 'd','d']
tmp.remove('d') #仅删除第一个出现的指定元素
print(tmp)


#永久性排序——sort
tmp = ['bmw','audi','toyota','subaru']
tmp.sort() #按字母顺序排序 
print(tmp)
tmp.sort(reverse=True) #逆序
print(tmp)


#暂时性排序——sorted
tmp = ['bmw','audi','toyota','subaru']
print(sorted(tmp,reverse=True))
print(tmp)

#倒转顺序——reverse
tmp = ['bmw','audi','toyota','subaru']
tmp.reverse()
print(tmp)
#reverse的作用是永久的，但显然，再次reverse一下即可复原

