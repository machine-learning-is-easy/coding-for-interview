

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        if abs(len(s) - len(t)) >= 2:
            return False

        i = len(s) - 1
        j = len(t) - 1
        while i >= 0 and j >= 0:
            if s[i] == t[j]:
                i -= 1
                j -= 1
            else:
                break

        if i < 0 or j < 0:
            return i == 0 or j == 0

        # i >= 0 and j >= 0 and s[i] != s[j]
        if i == j:
            return s[:i] == t[:j]
        elif i > j:
            return s[:i] == t[:j + 1]
        else:
            return s[:i + 1] == t[:j]