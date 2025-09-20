
from functools import lru_cache

class Solution:
    @lru_cache()
    def longestNiceSubstring(self, s: str) -> str:
        # Edge case
        if len(s) < 2:
            return ""

        nice = ""  # Store the longest nice substring
        for i in range(len(s)):
            # checking every character, upper case and lower case, if find one letter upper case or lower case is not
            # in the string, will split the string and recursive call left half and right half, find the maximum length
            # and return the maximum length
            if s[i].lower() in s and s[i].upper() in s:
                nice += s[i]
            else:
                leftPart = self.longestNiceSubstring(s[:i])
                rightPart = self.longestNiceSubstring(s[i + 1:])
                return leftPart if len(leftPart) >= len(rightPart) else rightPart
        return nice

assert Solution().longestNiceSubstring("YazaAay") == "aAa"