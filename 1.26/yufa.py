target = 4
a=  [1, 2, 3]
for num in a:
    b = []
    num2 = target - num

    if num2 in a:
        print(a.index(num))
        print(a.index(num2))
    break