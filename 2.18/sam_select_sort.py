def select_sort(li=list):
    new_li = []
    for i in range(len(li)):
        min_val = min(li)
        new_li.append(min_val)
        li.remove(min_val)
    return new_li

print(select_sort([1,5,6,8,9,4,87,9,6,4,3]))

def rightselect_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i],li[min_loc]=li[min_loc],li[i]

    return li

print(rightselect_sort([1,5,6,8,9,4,87,9,6,4,3]))