# 定义布尔型变量 has_ticket 表示是否有车票
# 定义整型变量 knife_length 表示刀的长度，单位：厘米
# 首先检查是否有车票，如果有，才允许进行 安检
# 安检时，需要检查刀的长度，判断是否超过 20 厘米
# 如果超过 20 厘米，提示刀的长度，不允许上车
# 如果不超过 20 厘米，安检通过
# 如果没有车票，不允许进门
has_ticket = False

knife_lenth =int(input('请输入刀的长度'))
if has_ticket:
    print('有车票才可以检查')
    if knife_lenth<20:
            print('安检通过')
    else:print('不允许上车')
else:
    print('不允许进门')


