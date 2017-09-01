'''
Created on Aug 31, 2017

@author: xp
'''
phone_book = {'tom':123, 'xp':333, 'xx':555}

print(phone_book.keys())

print(phone_book.get('xx'))

print(phone_book['xp'])


print(phone_book.get('xxx'))

mixed_dic = {'xx':123, 666:'jim'}

# mixed_dic.popitem()

# print(mixed_dic)

phone_book['lily'] = 123456

print(phone_book)

# 不能通过下表来访问
# print(phone_book[2])

del phone_book['xx']

print(phone_book)



