def mindiff(k,num):
    num.sort()
    return min(num[i+k-1]-num[i] for i in range(len(num)-k+1))


a= mindiff(4,[2,5,11,16,23])
print(a)

'''def minimumDifference(nums: list[int], k: int) -> int:
    nums.sort()
    return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))

a=minimumDifference([1,5,6,7,11,13,17],4)
print(a)
'''
