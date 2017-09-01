'''
Created on Aug 31, 2017

@author: xp
'''

# num = 59
# guess = int(input('输入一个整数！'))
# if guess == num:
#     print('猜对了')
# elif guess > num:
#     print("太大了")
# elif guess < num:
#     print('太小了')


# for循环

# for i in range(1,10):
#     print(i)
# else:
#     print('is done')

# list1 = [1, 2, 3, 4, 5, 6, 'aaaa', [123, 456]]
# for i in list1:
#     print(i)



# tuple1=(1,2,3,4,5,6,'1111','22222','33333')
# for i in tuple1:
#     print(i)


dict1 = {'xx':123, 'xp':[456], 'aa':'789'}

for key in dict1.keys():
    print(key)
    print(dict1[key])
    
for key, value in dict1.items():
    print(key, value)














