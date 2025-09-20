
import math

class Solution:
    def numSquares(self, n: int) -> int:

        results = []

        def recursive_find(target, res):

            max_root = int(math.sqrt(target)) + 1
            for i in range(2, max_root + 1):
                if target == i * i:
                    res.append(i)
                    results.append(list(res))
                    res.pop(-1)
                    return
                elif target < i * i:
                    break
                else:
                    res.append(i)
                    recursive_find(target - i * i, res)
                    res.pop(-1)

            return

        res = []
        recursive_find(n, res)

        return min([len(r) for r in results])


assert Solution().numSquares(12) == 3