

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        maxOneDel= [-1e10 for i in range(0, len(arr))]
        maxNoDel = [-1e10 for i in range(0, len(arr))]
        maxNoDel[0] = maxOneDel[0] = res = arr[0]

        for idx in range(1, len(arr)):
            maxNoDel[idx] = max(maxNoDel[idx - 1] + arr[idx], arr[idx])
            maxOneDel[idx] = max(maxNoDel[idx-1], maxOneDel[idx-1] + arr[idx])
            res = max(res, max(maxNoDel[idx], maxOneDel[idx]))
        return res


arr = [1,-2,0,3]

assert Solution().maximumSum(arr) == 4