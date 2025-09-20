
"""
starting from top left cell. BFS the right and down direction. add the the new element to a maximum heap. if the length of the heap is k and current cell 
value is greater than the first element of the heap stop the direction search
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        queue = [(matrix[0][0], 0, 0)]
        row = len(matrix)
        col = len(matrix[0])
        visited = set([(0.0)])
        count = 0
        while queue:
            _, r, c = heapq.heappop(queue)
            count += 1
            if count == k:
                return matrix[r][c]
            for dr, dc in [(0, 1), (1, 0)]:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < row and 0 <= new_c < col and (new_r, new_c) not in visited:
                    heapq.heappush(queue, (matrix[new_r][new_c], new_r, new_c))
                    visited.add((new_r, new_c))

        return -1

