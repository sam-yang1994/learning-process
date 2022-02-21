#在使用continue 关键字时需要特别注意变量计数是否修改  否则会死循环
i = 1
while i <= 10:

    if i == 3:
        i+=1
        continue

    print(i)
    i+=1
