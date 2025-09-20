
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0  # Left pointer of the sliding window
        bitmask = 0  # Stores the bitwise OR of the current subarray
        max_length = 0  # Stores the maximum length found

        for right in range(len(nums)):
            # If adding nums[right] creates a conflict, move left pointer
            while (bitmask & nums[right]) != 0:
                bitmask ^= nums[left]  # Remove nums[left] from the bitmask
                left += 1  # Move left pointer forward

            # Add nums[right] to the current bitmask
            bitmask |= nums[right]

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length