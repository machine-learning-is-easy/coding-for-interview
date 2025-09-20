

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col, level = len(maze) - 1, len(maze[0]) - 1, 1
        q = deque([(entrance[0], entrance[1])])
        maze[entrance[0]][entrance[1]] = "+"

        while q:
            for _ in range(len(q)):
                pr, pc = q.popleft()  # parent row and colomn
                for (x, y) in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    r, c = pr + x, pc + y
                    if r < 0 or r > row or c < 0 or c > col or maze[r][c] == "+":
                        continue
                    if r == 0 or r == row or c == 0 or c == col:
                        return level
                    maze[r][c] = "+"
                    q.append((r, c))
            level += 1

        return -1