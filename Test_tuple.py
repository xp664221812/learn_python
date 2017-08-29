'''
Created on Aug 30, 2017

@author: xp
'''
from builtins import str

# tuple是不能被更改的,但如果tuple中元素是集合，可以更改集合中的内容

# 创建只包含一个元素的tuple
a_tuple = (2,)

mix_tuple = (1, 2, 3, ['aaa', 5, 6, 6, 7])

print("mix_tuple=====" + str(mix_tuple))

# mix_tuple[4]=4
mix_tuple[3][0] = 'a'

print("mix_tuple after=====" + str(mix_tuple))








