

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # left and right pointer
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 == 1:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1

        return nums