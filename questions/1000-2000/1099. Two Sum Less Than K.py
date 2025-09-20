

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        Max = -1
        nums.sort()
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] + nums[j] > k:
                j -= 1
            elif nums[i] + nums[j] < k:
                if nums[i] + nums[j] > Max:
                    Max = nums[i] + nums[j]
                i += 1
            else:
                j -= 1

        return Max