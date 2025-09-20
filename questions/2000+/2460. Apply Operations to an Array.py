

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx - 1]:
                nums[idx - 1] = 2 * nums[idx - 1]
                nums[idx] = 0

        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] != 0:
                l += 1

            while l < r and nums[r] == 0:
                r -= 1

            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            else:
                break
        return nums
