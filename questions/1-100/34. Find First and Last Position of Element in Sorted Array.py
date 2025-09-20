

# in the edge case of [1, 1, 1, 1, 1, 1], target= 1. the time complexity is n not log(n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # find the index first

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid - 1
            elif nums[mid] > target:
                end = mid + 1
            else:
                # find the value search left and right index

                left = mid
                right = mid

                left_index = mid
                right_index = mid

                while left >= 0 and nums[left] == target:
                    left_index = left
                    left -= 1

                while right < len(nums) and nums[right] == target:
                    right_index = right
                    right += 1

                return [left_index, right_index]

        return [-1, -1]


assert Solution().searchRange([5,7,7,8,8,10], 8) == [[1,2]]


# binary search, in the test case [1, 1, 1, 1, 1, 1], target= 1. the time complexity is log(n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] >= target:
                right = mid - 1

        if 0 <= left < n and nums[left] == target:
            min_idx = left
        else:
            min_idx = -1

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        if 0 <= right < n and nums[right] == target:
            max_idx = right
        else:
            max_idx = -1

        return [min_idx, max_idx]