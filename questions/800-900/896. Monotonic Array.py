

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = True
        decrease = True

        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx - 1]:
                decrease = False
            if nums[idx] < nums[idx - 1]:
                increase = False
        return increase or decrease