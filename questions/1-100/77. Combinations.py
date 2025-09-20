

class Solution:
    def combine(self, n: int, k: int):

        nums = list(range(1, n + 1))

        def backtracking(res, position):
            if len(res) == k:
                result.append(list(res))
            else:
                for ind in range(position, n):
                    res.append(nums[ind])
                    backtracking(res, ind + 1)
                    res.pop(-1)

        result = []

        backtracking([], 0)

        return result

assert Solution().combine(4, 2) == [[1,2]]