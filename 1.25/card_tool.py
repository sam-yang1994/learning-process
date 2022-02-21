# **************************************************
# 欢迎使用【名片管理系统】V1.0
#
# 1. 新建名片
# 2. 显示全部
# 3. 查询名片
#
# 0. 退出系统
# **************************************************
card_list = []


def show_menu():
    print("*" * 50)
    print('欢迎使用【名片管理系统】V1.0')
    print('')
    print('1.新建名片')
    print('2.显示全部')
    print('3. 查询名片')
    print('')
    print('0. 退出系统')
    print("*" * 50)


def new_card():
    name = input('请输入姓名')
    phone = input('请输入电话')
    QQ = input('请输入QQ')
    email = input('请输入邮件')
    card_add = {'name':name, 'phone': phone, 'QQ':QQ, 'email':email}
    card_list.append(card_add)
    print(card_add)
    print("名片添加成功")


def card_look():
    mingzi = input("请输入要查找的名字")
    for ming in card_list:
        if ming["name"] == mingzi:
            print(ming)

def card_show():
    for al in card_list:
        print(al)




