

class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

"""
cache + dfs

questions: does the list contain multiple elements?

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)
        memo = {}

        def consecutive(n):
            if n in memo:
                return memo[n]
            else:
                total = 0
                if n not in num_set:
                    pass
                else:
                    total = 1 + consecutive(n - 1)
                memo[n] = total
                return total

        for num in num_set:
            longest_streak = max(longest_streak, consecutive(num))

        return longest_streak
