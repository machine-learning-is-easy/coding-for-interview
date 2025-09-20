
class Solution:
    def updateMatrix(self, mat: list) -> list:

        rows = len(mat)
        cols = len(mat[0])

        def bfs(r, c):
            if mat[r][c] == 0:
                return 0
            else:
                step = 0
                current_ele = [(r, c)]
                visited = set()
                visited.add((r, c))

                surroundings = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                while current_ele:
                    step += 1
                    for _ in range(len(current_ele)):
                        r, c = current_ele.pop(0)
                        for dx, dy in surroundings:
                            new_r, new_c = r + dx, c + dy
                            if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited:
                                if mat[new_r][new_c] == 0:
                                    return step
                                else:
                                    current_ele.append((new_r, new_c))
                                visited.add((new_r, new_c))

        res = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                res[r][c] = bfs(r, c)

        return res


"""
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""
mat = [[0,0,0],[0,1,0],[1,1,1]]

assert Solution().updateMatrix(mat) == [[0,0,0],[0,1,0],[1,2,1]]