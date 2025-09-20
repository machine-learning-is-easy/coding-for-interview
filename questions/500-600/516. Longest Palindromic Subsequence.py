

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        def dfs(i, j):
            if i < 0 or j >= len(s):
                return 0
            elif s[i] == s[j]:
                if i == j:
                    return 1 + dfs(i - 1, j + 1)
                else:
                    return 2 + dfs(i - 1, j + 1)
            else:
                return max(dfs(i - 1, j), dfs(i, j + 1))

        max_len = 0

        for ind in range(len(s)):
            max_len = max(max_len, dfs(ind, ind), dfs(ind, ind + 1))

        return max_len