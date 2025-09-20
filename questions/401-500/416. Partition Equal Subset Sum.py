

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 == 1:
            return False

        @cache  # lru_cache is worse than cache
        def dfs(i, target):
            if target == 0:
                return True
            else:
                if i == len(nums):
                    return False
                else:
                    if dfs(i + 1, target - nums[i]) or dfs(i + 1, target):
                        return True
                return False

        return dfs(0, sum(nums) // 2)