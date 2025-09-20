

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = 0
        zeros = 0
        while ind < len(nums) - zeros:
            if nums[ind] == 0:
                nums.pop(ind)
                nums.append(0)
                zeros += 1
            else:
                ind += 1
        return nums
