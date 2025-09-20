

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0

        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Check if the current cell is part of a battleship
                if board[i][j] == 'X':
                    # If it's the first part of the battleship (no 'X' to the left or above), count it
                    if i > 0 and board[i - 1][j] == 'X':  # Check if there's an 'X' directly above
                        continue
                    if j > 0 and board[i][j - 1] == 'X':  # Check if there's an 'X' directly to the left
                        continue
                    count += 1

        return count