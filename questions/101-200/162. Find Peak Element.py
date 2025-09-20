


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def search(nums: List[int], l: int, r: int) -> int:
            if l == r:
                return l

            mid = int((l + r) / 2)

            if (nums[mid] > nums[mid + 1]): # mid + 1 has to lower than
                return search(nums, l, mid)

            else:
                return search(nums, mid + 1, r)

        return search(nums, 0, len(nums) - 1)


# binary search solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] > nums[mid + 1]:
                right = mid

        return left