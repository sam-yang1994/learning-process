def linearsearch(arr,x):

    for i in range(len(arr)):
        if arr[i] == x:
            return i
    else:
        return -1


a= linearsearch([1,5,7,9,11],7)
print(a)