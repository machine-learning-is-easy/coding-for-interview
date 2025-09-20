


class Solution:
    def solveNQueens(self, n: int) -> list:
        # **********
        def could_place(row, col):
            return not (cols[col] + hill_diag[row - col] + dale_diag[row + col])

        def place_queen(row, col):
            queen_pos.append([row, col])
            cols[col] = 1
            hill_diag[row - col] = 1
            dale_diag[row + col] = 1

        def remove_queen(row, col):
            queen_pos.remove([row, col])
            cols[col] = 0
            hill_diag[row - col] = 0
            dale_diag[row + col] = 0

        def add_solution():
            solution.append(["." * col + 'Q' + '.' * (n - 1 - col) for _, col in queen_pos])

        def backtrack(row=0):
            for c in range(n):
                if could_place(row, c):
                    place_queen(row, c)
                    if row == n - 1:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, c)

        solution = []
        hill_diag = [0] * (2 * n - 1)  #
        dale_diag = [0] * (2 * n - 1)  #
        queen_pos = []
        cols = [0] * n
        backtrack()

        return solution
