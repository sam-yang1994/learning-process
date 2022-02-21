def onebite(bits):
    i = 0
    n = len(bits)
    while i < n-1:
        i += bits[i] + 1
    return i == n - 1

a=onebite([0,1,1,0,1,0,1,0,1])
print(a)
