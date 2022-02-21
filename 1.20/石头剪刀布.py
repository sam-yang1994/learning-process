import random

player = int(input('请输入你的选择（石头1，剪刀2，布3）'))
computer = random.randint(1,3)
print(computer)
if  player == computer:
    print('平局再来')
elif  (player==1 and computer == 2) or (player==2 and computer==3) or (player==3 and computer == 1):
    print('我真棒')
else:print('我要回去修炼了')