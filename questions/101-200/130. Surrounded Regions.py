

class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # DFS find all 'O's
        # if any elements is on boarder set all
        r_n = len(board) - 1
        c_n = len(board[0]) - 1

        def _dfs(node, visited):
            # find if node island is surrounded by "X"
            r, c = node
            if r < 0 or r > r_n or c < 0 or c > c_n:
                return

            if node not in visited:
                if board[r][c] == 'O':
                    visited.add(node)
                    _dfs((r - 1, c), visited)
                    _dfs((r + 1, c), visited)
                    _dfs((r, c - 1), visited)
                    _dfs((r, c + 1), visited)

        all_board = set()
        for r in range(r_n + 1):
            if board[r][0] == 'O':
                visited = set()
                _dfs((r, 0), visited)
                all_board = all_board.union(visited)

            if board[r][c_n] == 'O':
                visited = set()
                _dfs((r, c_n), visited)
                all_board = all_board.union(visited)

        for c in range(c_n + 1):
            if board[0][c] == 'O':
                visited = set()
                _dfs((0, c), visited)
                all_board = all_board.union(visited)

            if board[r_n][c] == 'O':
                visited = set()
                _dfs((r_n, c), visited)
                all_board = all_board.union(visited)

        for c in range(c_n + 1):
            for r in range(r_n + 1):
                if (r,c) not in all_board:
                    board[r][c] = "X"


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        memo = {}

        def dfs(r, c):
            if r <= row - 1 and r >= 0 and c <= col - 1 and c >= 0:
                if (r, c) in memo:
                    return memo[(r, c)]
                elif board[r][c] == "X":
                    return True
                elif board[r][c] == "O" and (r, c) not in current_visited:
                    current_visited.add((r, c))
                    return_ = dfs(r, c - 1) and dfs(r, c + 1) and dfs(r + 1, c) and dfs(r - 1, c)
                    memo[(r, c)] = return_
                    return return_
            else:
                return False

        findings = []
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    current_visited = set()
                    if (r, c) not in current_visited:
                        if dfs(r, c):
                            findings.append(list(current_visited))
        print(findings)
        for r, c in findings:
            board[r][c] = 'X'

        return board


# assert Solution().solve([["O"]]) == [["O"]]
assert Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]) == []
assert Solution().solve([["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]) == []