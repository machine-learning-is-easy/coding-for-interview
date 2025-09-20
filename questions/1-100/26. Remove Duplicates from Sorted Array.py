


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        ind = 0
        while ind < len(nums):
            if nums[ind] in nums[:ind]:
                nums.pop(ind)
            else:
                ind += 1


# take advantage of the sorted array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 1
        while ind < len(nums):
            if nums[ind] == nums[ind - 1]:
                nums.pop(ind)
            else:
                ind += 1
        return len(nums)