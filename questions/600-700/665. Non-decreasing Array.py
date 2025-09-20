
"""
TIPS: what about switch two elements
find the two index of decreasing order
switch two elements, check if follow non-decreasing order
"""
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        num_violations = 0
        for i in range(1, len(nums)):

            if nums[i - 1] > nums[i]:

                if num_violations == 1:
                    return False

                num_violations += 1

                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

        return True