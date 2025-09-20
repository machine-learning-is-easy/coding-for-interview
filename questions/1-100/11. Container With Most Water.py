'''

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea, l, r = 0, 0, len(height) - 1
        while l < r:
            maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxarea