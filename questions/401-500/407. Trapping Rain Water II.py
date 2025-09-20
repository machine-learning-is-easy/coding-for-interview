


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        # Initial
        # Board cells cannot trap the water
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        # Add Board cells first
        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1

            # Start from level 0
        level, res = 0, 0

        while heap:
            height, x, y = heapq.heappop(heap)
            level = max(height, level)  # always process the lowest level from heap, so need to keep the max

            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and heightMap[i][j] != -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))

                    # If cell's height smaller than the level, then it can trap the rain water
                    if heightMap[i][j] < level:
                        res += level - heightMap[i][j]

                    # Set the height to -1 if the cell is visited
                    heightMap[i][j] = -1

        return res