

class Solution:
    def numTrees(self, n: int) -> int:
        arr = [num + 1 for num in range(n)]
        @cache
        def bsf(i, j):
            if i == j:
                return 1
            res = 0
            for idx in range(i, j):
                res += bsf(i, idx) * bsf(idx + 1, j)
            return res
        return bsf(0, len(arr))

# without cache, time complexity is 2^n, with cache the time complexity is n^2
