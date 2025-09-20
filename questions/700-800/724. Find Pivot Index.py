
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left_val = 0
        right_val = sum(nums)
        ind = 0
        while ind < len(nums):
            right_val -= nums[ind]
            if ind > 0:
                left_val += nums[ind - 1]
            if left_val == right_val:
                return ind
            ind += 1
        return -1