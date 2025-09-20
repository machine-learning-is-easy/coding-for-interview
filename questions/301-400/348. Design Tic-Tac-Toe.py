

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        to_add = 1 if player == 1 else -1
        self.row[row] += to_add
        self.col[col] += to_add
        if row == col:
            self.diag += to_add
        if row + col == self.n - 1:
            self.anti_diag += to_add
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diag) == self.n or abs(self.anti_diag) == self.n:
            return player
        return 0