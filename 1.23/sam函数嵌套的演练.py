def print_line(patten, times, line):
    while line > 0:
        print(patten * times)
        line -= 1


print_line('9', 60, 1)


def print_line1(tuan, cishu):
    """
dayin
    :param tuan:
    :param cishu:
    """
    print(tuan * cishu)


i = 0
while i < 5:

    print_line1("+", 4)
    i += 1
