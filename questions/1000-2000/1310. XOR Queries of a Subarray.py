

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []

        for left, right in queries:
            ans = 0
            for ind in range(left, right + 1):
                ans = ans ^ arr[ind]
            res.append(ans)

        return res