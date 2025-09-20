

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        live_cell = []
        dead_cell = []

        m = len(board)
        n = len(board[0])

        sourrounding_dir = [(-1, -1), (-1, 0), (-1, 1),
                            (0, -1), (0, 1),
                            (1, -1), (1, 0), (1, 1)
                            ]

        def check_status(i, j):

            active_cell = 0
            for cell in sourrounding_dir:
                x = i + cell[0]
                y = j + cell[1]
                if x >= 0 and x < m and y >= 0 and y < n:
                    if board[x][y] == 1:
                        active_cell += 1
            if board[i][j] == 1:
                if active_cell < 2:
                    return 0
                elif active_cell <= 3:
                    return 1
                else:
                    return 0
            else:
                if active_cell == 3:
                    return 1
                else:
                    return 0

        # find the live_cells and dead cells

        for i in range(m):
            for j in range(n):
                status = check_status(i, j)
                if status == 1:
                    live_cell.append((i, j))
                else:
                    dead_cell.append((i, j))

        for i, j in live_cell:
            board[i][j] = 1

        for i, j in dead_cell:
            board[i][j] = 0