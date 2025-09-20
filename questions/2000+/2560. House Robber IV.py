

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canRob(capcity):
            idx = 0
            count = 0
            while idx < len(nums):
                if nums[idx] <= capcity:
                    idx += 1
                    count += 1
                idx += 1
            return count >= k

        l, r = 0, max(nums)
        while l <= r:
            mid = (l + r) // 2
            if not canRob(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l
    