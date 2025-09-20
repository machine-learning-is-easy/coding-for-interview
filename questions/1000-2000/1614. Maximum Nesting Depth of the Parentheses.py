
class Solution:
    def maxDepth(self, s: str) -> int:
        v = 0
        res = 0

        # Handle base case
        if not s:
            return 0

        # Iterate through the string
        for i in s:
            if i == '(':
                v += 1
                res = max(res, v)
            elif i == ')':
                v -= 1
        return res