

class Solution:
    def numTeams(self, rating: List[int]) -> int:

        res = 0

        # increase pattern
        def dfs(ind, val, n):
            nonlocal res
            if n == 0:
                res += 1
            else:
                for r_ind in range(ind, len(rating)):
                    if rating[r_ind] > val:
                        dfs(r_ind, rating[r_ind], n - 1)

        dfs(0, float("-inf"), 3)

        # dncrease pattern
        def dfs(ind, val, n):
            nonlocal res
            if n == 0:
                res += 1
            else:
                for r_ind in range(ind, len(rating)):
                    if rating[r_ind] < val:
                        dfs(r_ind, rating[r_ind], n - 1)

        dfs(0, float("inf"), 3)

        return res

# a concise version

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result = 0

        for idx, middle in enumerate(rating):
            a = sum(left < middle for jdx, left in enumerate(rating[:idx]))
            b = sum(left > middle for jdx, left in enumerate(rating[:idx]))
            c = sum(right < middle for jdx, right in enumerate(rating[idx + 1:]))
            d = sum(middle < right for jdx, right in enumerate(rating[idx + 1:]))
            result += a * d + b * c

        return result
