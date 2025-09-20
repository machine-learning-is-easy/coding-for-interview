

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0

            # Merge boxes of same color as boxes[l] at the start
            while l < r and boxes[l] == boxes[l + 1]:
                l += 1
                k += 1

            # Option 1: remove boxes[l]...boxes[l+k] now
            res = (k + 1) ** 2 + dp(l + 1, r, 0)

            # Option 2: try to merge later matching boxes
            for m in range(l + 1, r + 1):
                if boxes[m] == boxes[l]:
                    res = max(res, dp(l + 1, m - 1, 0) + dp(m, r, k + 1))

            return res

        return dp(0, len(boxes) - 1, 0)