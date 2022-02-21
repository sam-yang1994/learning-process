# 使用input函数接受用户输入，用户输入月份和日期，比如“3月15日”，请写程序判断这个日期是否合法，为了简化编程难度， 只考虑非闰年的情况，默认月份总是正确。以下为输入示例、
month = int (input('请输入月份'))
day = int (input('请输入日期'))
if month in (1,3,5,7,8,10,12):
    if 0<day<=31:
       print('日期合法')
    else:print('日期不合法')
elif month in (4,6,9,11):
    if 0<day<=30:
        print('日期合法')
    else:print('日期不合法')
else:print('日期不合法')


