"""
Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[l]:
                # the array is rotated, mid, r is in ordered
                # the minimum is between l, mid
                minimum = min(minimum, nums[mid])
                r = mid - 1

            elif nums[mid] > nums[l]:
                # left half is ordered
                if nums[mid] > nums[r]:
                    # the array is rotated:
                    # minimum is between mid, r
                    minimum = min(minimum, nums[l])
                    l = mid + 1

                elif nums[mid] < nums[r]:
                    # the array is fully ordered
                    return min(minimum, nums[l])
                else:
                    minimum = min(minimum, nums[r])
                    r -= 1

            else:
                minimum = min(minimum, nums[l])
                l += 1

        return minimum


assert Solution().findMin([3,1]) == 1