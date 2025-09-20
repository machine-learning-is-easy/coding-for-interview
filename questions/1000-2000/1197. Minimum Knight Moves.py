

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)  # Only need to consider first quadrant
        directions = [
            (1, 2), (2, 1), (-1, 2), (-2, 1),
            (1, -2), (2, -1), (-1, -2), (-2, -1)
        ]

        visited = set()
        queue = deque([(0, 0, 0)])  # (current_x, current_y, steps)

        while queue:
            curr_x, curr_y, steps = queue.popleft()
            if (curr_x, curr_y) == (x, y):
                return steps
            for dx, dy in directions:
                nx, ny = curr_x + dx, curr_y + dy
                # Prune search space to a reasonable bound
                if (nx, ny) not in visited and nx >= -1 and ny >= -1:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))