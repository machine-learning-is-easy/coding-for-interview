

# if logn runtime complexity, need binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid

        return -1