

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        stack = []

        for idx in range(n - 1, -1, -1):
            count = 0
            while stack and stack[-1] < heights[idx]:
                stack.pop(-1)
                count += 1
            if stack:
                count += 1
            res[idx] = count

        return count