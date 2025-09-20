

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)  # Sentinel to clear stack at end

            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
            heights.pop()  # Clean up sentinel
            return max_area

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_rect = 0

        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            max_rect = max(max_rect, largestRectangleArea(heights))

        return max_rect