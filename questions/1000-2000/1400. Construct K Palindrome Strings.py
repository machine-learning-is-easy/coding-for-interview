
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
                # Handle edge cases
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        # Initialize frequency dictionary and odd_count
        freq = [0] * 26
        odd_count = 0

        # Increment the value of the index corresponding to the current character
        for char in s:
            freq[ord(char) - ord("a")] += 1
        # Count the number of characters that appear an odd number of times in s
        for count in freq:
            if count % 2 == 1:
                odd_count += 1
        # Return if the number of odd frequencies is less than or equal to k
        return odd_count <= k