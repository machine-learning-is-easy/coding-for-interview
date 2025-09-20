
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

        max_length = 0

        # Iterate over each possible remainder value from 0 to k-1
        for target_remainder in range(k):

            # Initialize the dynamic programming array to store the maximum length for each remainder
            dp = [0] * k

            # Iterate over each number in the input array
            for num in nums:
                # Calculate the remainder of the current number when divided by k
                current_remainder = num % k

                # Calculate the remainder that would achieve the target remainder when added to the current number
                previous_remainder = (target_remainder - num) % k

                # Update the dp array
                dp[current_remainder] = max(dp[current_remainder], dp[previous_remainder] + 1)

            # Update the result with the maximum value found in the dp array for the current target remainder
            max_length = max(max_length, max(dp))

        return max_length