

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        start = 0
        total = 0
        current_sum = 0

        for end in range(len(nums)):
            current_sum += nums[end]
            # Shrink window from the left if score is too high
            while current_sum * (end - start + 1) >= k:
                current_sum -= nums[start]
                start += 1
            # Count all valid subarrays ending at 'end'
            total += (end - start + 1)

        return total