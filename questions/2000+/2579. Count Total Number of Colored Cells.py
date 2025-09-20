

class Solution:
    def coloredCells(self, n: int) -> int:
        if n <= 0:
            return 0
        visited = set([0, 0])
        queue = []
        queue.append((0, 0))
        sur = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        step = 1
        while step < n:
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                for dx, dy in sur:
                    new_x, new_y = x + dx, y + dy
                    if (new_x, new_y) not in visited:
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
            step += 1
        return len(visited)