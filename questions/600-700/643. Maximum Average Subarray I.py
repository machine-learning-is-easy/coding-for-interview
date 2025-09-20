

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = curr_sum = sum(nums[:k])

        # Slide the window across the array
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]  # Add new element, remove old one
            max_sum = max(max_sum, curr_sum)

        # Return the maximum average value
        return max_sum / k
