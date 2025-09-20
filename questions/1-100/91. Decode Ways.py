

# ask question if 06 valid or not.

class Solution:
    def __init__(self):
        self.memo = {}

    def recursive_with_memo(self, index, s) -> int:
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0

        if index == len(s) - 1:
            return 1

        # Memoization is needed since we might encounter the same sub-string.
        if index in self.memo:
            return self.memo[index]

        ans = self.recursive_with_memo(index + 1, s) \
              + (self.recursive_with_memo(index + 2, s) if (int(s[index: index + 2]) <= 26) else 0)

        # Save for memoization
        self.memo[index] = ans

        return ans

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        return self.recursive_with_memo(0, s)


# DFS
class Solution:
    def numDecodings(self, s: str) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(i):
            # Base case: reached end of string => 1 valid way
            if i == len(s):
                return 1
            # If starts with '0', no valid decoding
            if s[i] == '0':
                return 0

            # Take one digit
            res = dfs(i + 1)

            # Take two digits if it's a valid number <= 26
            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                res += dfs(i + 2)

            return res

        return dfs(0)

# DP solution
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)

        # Base cases
        dp[0] = 1  # Empty string has one way to decode
        dp[1] = 1  # First char is guaranteed not '0' here

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2:i])

            # Check single digit (must not be '0')
            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]

            # Check two digits (must be between 10 and 26)
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

