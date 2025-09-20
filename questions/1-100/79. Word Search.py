
"""
question: Is the word case sensitive?
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def backtrack(curr, suffix):
            # curr is the current pointer
            if not suffix:
                return True

            else:
                next_c = suffix[0]

                # find all the position of next is equal next_c around curr
                surround_position = [(curr[0] + i, curr[1] + j) for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]]
                surround_c = [(i, j) for i, j in surround_position if i >= 0 and i < rows and j >= 0 and
                              j < cols and board[i][j] == next_c and board_seen[i][j] is False]

                if not surround_c:
                    return False
                else:
                    for new_curr in surround_c:
                        board_seen[new_curr[0]][new_curr[1]] = True
                        if backtrack(new_curr, suffix=suffix[1:]):
                            return True
                        board_seen[new_curr[0]][new_curr[1]] = False
                return False

        rows = len(board)
        cols = len(board[0])
        board_seen = [[False] * cols for _ in range(rows)]

        curr_list = [(i, j) for i in range(rows) for j in range(cols) if board[i][j] == word[0]]
        for p in curr_list:
            i, j = p
            board_seen[i][j] = True
            if backtrack(p, word[1:]):
                return True
            board_seen[i][j] = False
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row = len(board)
        col = len(board[0])
        visited = set()

        def dfs(r, c, word):
            if not word:
                return True
            if not (0 <= r < row and 0 <= c < col):
                return False
            if board[r][c] == word[0] and (r, c) not in visited:
                visited.add((r, c))
                for neig in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if dfs(neig[0], neig[1], word[1:]):
                        return True
                visited.remove((r, c))
                return False
            else:
                return False

        for r in range(row):
            for c in range(col):
                if dfs(r, c, word):
                    return True

        return False
