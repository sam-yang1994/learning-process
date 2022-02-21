def measure():
    print('测量开始')
    tem = 40
    wetness = 50
    print('测量结束')
    return tem, wetness


result = measure()

print(result)

#当我们需要单独接受元组中的单个结果时
print(result[0])
#使用多个变量来接收结果，使用全局变量
gl_tem, gl_wet = measure()

print(gl_tem)
print(gl_wet)
