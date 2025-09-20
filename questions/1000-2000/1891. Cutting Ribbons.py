

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l, r = 1, max(ribbons)
        while l <= r:
            m = (l + r) // 2
            if sum([r // m for r in ribbons]) < k:
                r = m - 1
            else:
                l = m + 1
        return r