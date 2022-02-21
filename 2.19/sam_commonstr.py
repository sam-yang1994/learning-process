def commom_str(strs):

    lenth = len(strs[0])
    count = len(strs)
    for i in range(lenth):
        c = strs[0][i]

        if any(i == len(strs[j]) or strs[j][i] != c for j in range(1,count)):
            return strs[0][:i]

    return strs[0]
res = commom_str(['star','st'])
print(res)