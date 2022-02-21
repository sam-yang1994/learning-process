def sum_two(target,num):
    n = len(num)

    for i in range(n):
        for j in range(i+1,n):
            if num[i] + num[j] == target:
                return [i, j]



a = sum_two(7,[1,5,6,9,12])
print(a)