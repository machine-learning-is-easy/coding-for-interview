

class Solution(object):
    @lru_cache()
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

class Solution:

    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True  # empty string matches empty pattern

        # deal with patterns like a*, a*b*, a*b*c*, etc
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # fill dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]  # zero occurrence
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] |= dp[i - 1][j]  # one or more occurrence

        return dp[m][n]