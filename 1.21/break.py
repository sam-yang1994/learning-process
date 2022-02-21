num = 0
result = 0
while num <= 100:
    if num % 2 == 0:
       result += num
    num +=1
    if num == 12:
        break
print(result)