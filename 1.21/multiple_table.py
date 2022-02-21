def multiple_tabel():
    i = 1
    while i <= 9:
        a = 1
        while a <= i:
            print('%d*%d=%d' % (i, a, a*i), end="\t")
            a += 1
        print("")
        i += 1
