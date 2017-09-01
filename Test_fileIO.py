'''
Created on Sep 1, 2017

@author: xp
'''
# some_sentence = '''
#     1111111111111111111
#     2222222222222222222
#     3333333333333333333
#     '''
# f = open('/home/xp/ccc.txt', 'w')
#  
# f.write(some_sentence);
#  
# f.close()



f = open('/home/xp/ccc.txt', 'r')
  
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
  
f.close()


