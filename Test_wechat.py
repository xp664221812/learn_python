'''
Created on 2017年9月18日

@author: xp
'''
import itchat
from itchat.content import *

my = itchat.new_instance()

my.auto_login(hotReload=False, enableCmdQR=-2)

print('1111111111111111111111111')

def update_my_infos():
    """
    更新信息
    """
    # 获取并更新通讯录: {UserName: UserInstance}
    my.friends = {user["UserName"]: user for user in my.get_friends(update=True)}
    # 获取并更新群列表: {UserName: UserInstance}
    my.groups = {group["UserName"]: group for group in my.get_chatrooms(update=True)}
    
    print(123456)
    
    return
update_my_infos()