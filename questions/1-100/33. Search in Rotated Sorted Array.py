

# pay attention if there is duplicate elements in the rotated sorted array
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while start <= end:

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[start]:  # becareful >=
                # left half is in order
                if target < nums[mid] and target >= nums[start]:  # be careful >=
                    end = mid - 1  # be careful -1
                else:
                    start = mid + 1

            else:
                # right side is in order
                if target > nums[mid] and target <= nums[end]: # be careful <=
                    start = mid + 1
                else:
                    end = mid - 1

        return -1