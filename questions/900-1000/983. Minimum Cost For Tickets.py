

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(day, i):
            if i >= len(days):
                return 0
            if day > days[i]:
                return dp(day, i + 1)
            return min([
                costs[0] + dp(days[i] + 1, i + 1),
                costs[1] + dp(days[i] + 7, i + 1),
                costs[2] + dp(days[i] + 30, i + 1)
            ])

        return dp(0, 0)