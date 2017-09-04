'''
Created on Sep 4, 2017

@author: xp
'''
class Student:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        
    def sayHi(self):
        print('my name is ',self.name,',i am ',self.age)

student1 = Student('xp', 18)

student1.sayHi()
