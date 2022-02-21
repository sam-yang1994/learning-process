def sum_number(n):
    m = 0
    num = 0
    while m <= n:
        num += m
        m += 1
    print(num)


sum_number(15)

'''def sum_digui(a):

    sum = + sum_digui(a)
    if a == 1:
        return
    sum_digui(a-1)


sum_digui(15)'''

def sum_digui(a):

    if a == 1:
        return 1

    tem = sum_digui(a-1)

    return a + tem


result=sum_digui(100)
print(result)