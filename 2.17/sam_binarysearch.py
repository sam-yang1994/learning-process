def binary_search(arr,val):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == val :
            return mid
        elif arr[mid] < val:
            left = mid + 1
        elif arr[mid] > val:
            right = mid - 1
    else:
        return "没有需要查找的值"

print(binary_search([1,5,7,46,56,99],56))