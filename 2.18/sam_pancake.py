class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)):
            max_id = arr.index(max(arr))
            res.append(max_id+1)
            res.append(len(arr))
            arr[:max_id]= arr [max_id::-1]
            arr=arr[::-1]
            arr.pop()
        return res
