

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        @cache
        def calc(i, j):
            if i == n or j == m:
                return max(n - i, m - j)
            if word1[i] == word2[j]:
                return calc(i + 1, j + 1)
            else:
                return min(calc(i + 1, j), calc(i, j + 1)) + 1
        return calc(0, 0)