'''
Created on Aug 31, 2017

@author: xp
'''
from pyparsing import nums
def repeat_str(s, num=1):
    return s * num


print(repeat_str('xp', 10))

print(repeat_str('hello'))


def func(a, b=4, c=8):
    print('a is ', a, 'b is ', b, 'c is ', c)

func(1, 9)

func(6, c=7)



def print_params(fpara, *nums, **words):
    print('fpara is ', fpara)
    print('nums is ', nums)
    print('words id ', words)



print_params('xxx', 1, 2, 'a', 4, 5, words='123', another_word='456')










