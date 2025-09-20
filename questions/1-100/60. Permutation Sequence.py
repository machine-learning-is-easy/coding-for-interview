

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        res = []
        nums = [str(_) for _ in range(1, n + 1)]

        def dfs(start):
            if start == n:
                res.append("".join(nums))

            if len(res) == k:
                return True
            else:
                for next_ind in range(start, n):
                    nums[next_ind], nums[start] = nums[start], nums[next_ind]
                    if dfs(start + 1):
                        return True
                    nums[start], nums[next_ind] = nums[next_ind], nums[start]

                return False

        dfs(0)
        return res[-1]