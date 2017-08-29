'''
Created on Aug 21, 2017

@author: xp
'''
import os
import requests

print('hello world')

print(os.getcwd())

r=requests.get('http://wwww.baidu.com')

print(r.text)