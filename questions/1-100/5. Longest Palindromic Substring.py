

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        elif len(s) == 1:
            return s
        else:
            l = len(s)
            dp = [[False] * l for i in range(l)]

            for i in range(l):
                dp[i][i] = True
                if i + 1 < l and s[i + 1] == s[i]:
                    dp[i + 1][i] = True

            x, y = 0, 0
            for j in range(1, l):
                for i in range(j - 1, -1, -1):
                    if dp[i + 1][j - 1] and s[j] == s[i]:
                        dp[i][j] = True
                        if j - i >= y - x:
                            x, y = i, j

            return s[x:y + 1]


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandaroundcenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        if not s and len(s) < 1:
            return ''
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = expandaroundcenter(s, i, i)
            len2 = expandaroundcenter(s, i, i + 1)

            max_len = max(len1, len2)
            if max_len > end - start:
                if len1 > len2:
                    start = i - (max_len - 1) // 2
                    end = i + (max_len - 1) // 2
                else:
                    start = i - max_len // 2 + 1
                    end = i + max_len // 2

        return s[start:end + 1]

# revise edition, keep the longest palindrome during the expand process
class Solution(object):
    def longestPalindrome(self, s):
        """
                :type s: str
                :rtype: str
                """
        ans = ""
        max_len = 0
        def expandaroundcenter(s, left, right):
            nonlocal max_len
            nonlocal ans
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    ans = s[left: right + 1]
                left -= 1
                right += 1

        for ind in range(len(s)):
            expandaroundcenter(s, ind, ind)
            expandaroundcenter(s, ind, ind + 1)
        return ans

assert Solution().longestPalindrome('bb') == 'bb'


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        # Preprocess the string
        T = "^#" + "#".join(s) + "#$"
        n = len(T)
        P = [0] * n
        C = 0  # Center of current palindrome
        R = 0  # Right edge of current palindrome

        for i in range(1, n - 1):
            mirror = 2 * C - i

            if i < R:
                P[i] = min(R - i, P[mirror])

            # Expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # Update center and right edge
            if i + P[i] > R:
                C = i
                R = i + P[i]

        # Find the maximum element in P
        max_len = max(P)
        center_index = P.index(max_len)

        # Extract start position in original string
        start = (center_index - max_len) // 2
        return s[start:start + max_len]

s = "babad"
assert Solution().longestPalindrome(s) == "bab"