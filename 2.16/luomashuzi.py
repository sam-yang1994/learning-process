# class Solution:
#     def romanToInt(self, s: str) -> int:
#         dic = { 'M' : 1000,
#                 'D' : 500,
#                 'C' : 100,
#                 'L' : 50,
#                 'X' : 10,
#                 'V' : 5,
#                 'I' : 1
#         }
#         #罗马数字的规律就是放在左侧就是减，放在右侧就是加
#         res = 0
#         n = len(s)
#         for i in range(n - 1):
#             if dic[s[i]] < dic[s[i+1]]:
#                 res -= dic[s[i]]
#             else:
#                 res += dic[s[i]]
#         res += dic[s[n-1]]
#         return res


def romanToInt(s):
    diction = {'I':1,
               'V':5,
               'X':10,
               'L':50,
               'C':100,
               'D':500,
               'M':1000}

    res = 0
    n = len(s)
    for i in range(n-1):
        if diction[s[i]] <diction[s[i+1]]:
            res -= diction[s[i]]
        else:
            res += diction[s[i]]

    res += diction[s[n-1]]
    return res

IX