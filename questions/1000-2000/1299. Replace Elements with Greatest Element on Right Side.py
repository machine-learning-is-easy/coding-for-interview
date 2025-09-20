

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        max_v = -1
        res = [max_v] * l
        for ind in range(l - 1, -1, -1):
            res[ind] = max_v
            max_v = max(arr[ind], max_v)

        return res