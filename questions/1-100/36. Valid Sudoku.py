

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def ij2boxindex(i, j):
            # convert i, j to the index of the box
            return i // 3 * 3 + j // 3

        N = len(board)
        # initialize each row and columns and boxes dict, the key is the number, if find the number, +1, if the value is
        # greater than 1, then find multiple times of current key, validate the rule. return directly.
        # defaultdict(int) is a dict of unknown keys
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]

        # construct the rows, columns and boxes

        for r in range(N):
            for c in range(N):
                v = board[r][c]
                if v != ".":
                    # put value to rows:
                    rows[r][v] += 1
                    if rows[r][v] > 1:
                        print("row validation")
                        print(rows)
                        return False

                    columns[c][v] += 1
                    if columns[c][v] > 1:
                        print("column validation")
                        return False

                    boxind = ij2boxindex(r, c)
                    boxes[boxind][v] += 1
                    if boxes[boxind][v] > 1:
                        print("box validation")
                        return False
        return True