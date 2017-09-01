'''
Created on Aug 31, 2017

@author: xp
'''
num = 59
while(True):
    try:
        guess = int(input('输入一个整数！'))
        if guess == num:
            print('猜对了')
            break;
        elif guess > num:
            print("太大了")
        elif guess < num:
            print('太小了')
    except ValueError:
        print('您输入的不是数字!')
        

