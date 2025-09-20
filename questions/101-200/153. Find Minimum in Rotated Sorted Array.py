
"""
Qestions: Does the array include duplicate elements? 

"""

class Solution:
    def findMin(self, nums) -> int:

        length = len(nums)
        l, r = 0, length - 1
        min_val = nums[0]
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[l]:  # right half is ordered
                min_val = min(nums[mid], min_val, nums[r])
                r = mid - 1
            else:  # left half is ordered
                if nums[mid] < nums[r]:  # right half is ordered and left half is ordered
                    return min(min_val, nums[l])
                else:  # right half is not ordered
                    l = mid + 1
                    min_val = min(nums[mid], min_val, nums[l])
        return min_val

assert Solution().findMin([4,5,1,2,3]) == 1


## another version to check the logic. it is easier to check the minimum
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_val = nums[0]
        while l < r:
            mid = (l + r)//2
            min_val = min(min_val, nums[mid], nums[l], nums[r])
            if nums[mid] < nums[l]:
                r = mid - 1
            elif nums[mid] == nums[l]:
                l += 1
            else:
                if nums[r] > nums[mid]:
                    return min_val
                elif nums[r] == nums[mid]:
                    r -= 1
                else:
                    l = mid + 1
        return min_val