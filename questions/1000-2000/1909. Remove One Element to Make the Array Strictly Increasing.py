
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed_once = False
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                if removed_once:
                    # the second time to see a lower value.
                    return False
                if i > 1 and nums[i] <= nums[i - 2]:
                    # remove i
                    nums[i] = nums[i - 1]
                # the first delete.
                removed_once = True
        return True