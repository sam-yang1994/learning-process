i = 9
while i >=1:
    a = 9
    while a >= i:
        print('%d*%d=%d'% (i,a,a*i),end="\t")
        a-=1
    print('')
    i-=1