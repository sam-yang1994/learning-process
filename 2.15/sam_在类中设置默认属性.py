class cat:

    def __init__(self):

        print('这是一个初始化方法')
        self.name = 'Tom'

# 初始化方法会自动调用
tom = cat()
print(tom.name)