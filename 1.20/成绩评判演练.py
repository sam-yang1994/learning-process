# 定义两科math,english 变量只要有一科及格就及格
math = int(input('你的数学成绩是'))
english = int(input('你的英语成绩是'))
if math >= 60 or english >= 60:
    print("成绩合格")
else:print('小心回家挨打')