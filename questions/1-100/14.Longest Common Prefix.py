
"""
can use binary search, the question is how to use binary search
"""

def longestCommonPrefix(strs):
    if not strs:
        return ''
    min_len = min([len(s) for s in strs])
    left, right = 0, min_len
    while left < right:
        mid = (left + right + 1) // 2
        if all([s[:mid] == strs[0][:mid] for s in strs]):
            left = mid
        else:
            right = mid - 1
    return strs[0][:left]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ''
        for ws in zip(*strs):
            # all the string has the value and
            if len(ws) == len(strs) and len(set(ws)) == 1:
                res += ws[0]
            else:
                break
        return res

# another version of binary search
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        left = 0
        right = min([len(s) for s in strs])

        while left <= right:
            mid = (left + right) // 2
            if all([s[:mid] == strs[0][:mid] for s in strs]):
                left = mid + 1
            else:
                right = mid - 1
        return strs[0][:right]