

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            # the condition is very important, if out of the loop, nums[l] is the first element which is greater than target
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:  # end of the loop, nums[r] will be the first element which less than the target
                r = mid - 1
            else:
                return mid

        return l