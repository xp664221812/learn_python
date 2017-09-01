'''
Created on 2017年8月31日

@author: xp
'''
from builtins import str

def say_hello(content):
    print(content)
    
say_hello('1111111')


def plus(a, b):
    return a + b    

print(plus('xx', 'yyyy'))

x = 100

def test_glob1():
    x = 90
    print('x===' + str(x))


def test_glob2():
    print('x====' + str(x))
    
    
def test_glob3():
    global x
    x = 10

   
    
test_glob1()

test_glob2()

test_glob3()

print('x====' + str(x))








    




