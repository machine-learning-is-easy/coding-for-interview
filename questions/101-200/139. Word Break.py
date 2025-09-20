
# questions: letter case sensitive or no sensitive.
# what is the return of empty dicitionary, or empty string
class Solution:
    @lru_cache()
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        else:
            for w in wordDict:
                if s.startswith(w):
                    if self.wordBreak(s[len(w):], wordDict):
                        return True

        return False

# questions: do we need to use the dictionary once or multiple times?
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache()
        def dfs(s):
            if not s:
                return True
            else:
                for word in wordDict:
                    if s.startswith(word) and dfs(s[len(word):]):
                        return True

        return dfs(s)
# time complexity is O(N * M) where N is the length of the string s
# n = length of string s.
# m = number of words in the dictionary wordDict.

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # For O(1) lookups
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string is segmentable

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Found a valid segmentation up to i

        return dp[n]