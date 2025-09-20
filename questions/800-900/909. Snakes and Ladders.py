

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coords(s):
            """Convert square number s to board coordinates (r, c)"""
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if row % 2 != n % 2 else n - 1 - rem
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # (square, steps)

        while queue:
            square, steps = queue.popleft()
            for move in range(1, 7):
                next_square = square + move
                if next_square > n * n:
                    continue
                r, c = get_coords(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == n * n:
                    return steps + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, steps + 1))

        return -1