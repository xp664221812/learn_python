'''
Created on 2017年9月1日

@author: xp
'''
a = 5
b = 0

try:
    a / b
except ZeroDivisionError:
    print('除数不能为零')
    
