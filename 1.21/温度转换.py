tem =input()
if tem [-1] in ['f','F']:
    c = (int(tem[0:-1]) - 32)/1.8
    print(c,format('C'))

elif tem [-1] in ['c','C']:
     b= int(tem[0:-1])*1.8 + 32
     print(b,format('F'))
else:print('格式错误')
