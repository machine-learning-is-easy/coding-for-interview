
# option 1: start from end
# option 2: start from begining

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        memo = [0 for _ in range(l)]
        for i in range(l):
            memo[i] = -1
        memo[l-1] = 1
        for i in range(l-2, -1, -1):
            farjump = min(i+nums[i], l-1)
            for j in range(i +1, farjump + 1):
                if memo[j] == 1:
                    memo[i] = 1
                    break

        return memo[0] == 1

# more concise version
# if the index is far than reachable index, it will return False
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        reachable_idx = 0
        for i, num in enumerate(nums):
            if i > reachable_idx:
                return False  # Can't move past the current index
            reachable_idx = max(reachable_idx, i + num)
        return reachable_idx >= len(nums) - 1