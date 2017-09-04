'''
Created on 2017年9月4日

@author: xp
'''
class Spam(object):
    def doit(self, message):
        print(message)
#不带self的是静态方法
    def selfless(message):  # @NoSelf
        print(message)
        
        
obj = Spam()
x = obj.doit
x('hello world')

Spam.selfless('xxxxxxx')

# x = Spam.doit()
# x(obj, "hello world")
