

class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        max_len = 0

        # Step 1: Try to match suffix of s and reversed prefix of t
        for i in range(len(s)):
            for j in range(len(t)):
                l, r = 0, 0
                while i + l < len(s) and j - r >= 0 and s[i + l] == t[j - r]:
                    l += 1
                    r += 1
                    max_len = max(max_len, 2 * l)

        # Step 2: Check all palindromic substrings in s
        for start in range(len(s)):
            for end in range(start, len(s)):
                sub = s[start:end+1]
                if sub == sub[::-1]:
                    max_len = max(max_len, len(sub))

        # Step 3: Check all palindromic substrings in t
        for start in range(len(t)):
            for end in range(start, len(t)):
                sub = t[start:end+1]
                if sub == sub[::-1]:
                    max_len = max(max_len, len(sub))

        return max_len