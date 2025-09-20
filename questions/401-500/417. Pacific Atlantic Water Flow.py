

class Solution:
    def pacificAtlantic(self, heights: list) -> list:
        # DFS searching for every element of the matrix

        def dfs(i, j, visited, height):
            if not (0 <= i < R and 0 <= j < C and heights[i][j] >= height and (i, j) not in visited):
                return

            visited.add((i, j))

            for r, c in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                dfs(i + r, j + c, visited, heights[i][j])

        R, C = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        for i in range(C):
            dfs(0, i, pacific, -1)
            dfs(R - 1, i, atlantic, -1)
        for i in range(R):
            dfs(i, 0, pacific, -1)
            dfs(i, C - 1, atlantic, -1)

        return pacific & atlantic

assert Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]) == \
       [[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]]