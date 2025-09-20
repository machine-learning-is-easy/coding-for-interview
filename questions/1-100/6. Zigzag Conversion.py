
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        output = [[] for _ in range(numRows)]

        ind_sub_list = 0
        direction = 1

        for s_i in s:
            output[ind_sub_list].append(s_i)
            if ind_sub_list + direction >= len(output) or ind_sub_list + direction < 0:
                direction = -1 * direction
            ind_sub_list = ind_sub_list + direction
        return ''.join(["".join(l) for l in output])


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        curr_row = 0
        going_down = False

        for c in s:
            rows[curr_row] += c
            # If we're at top or bottom, reverse the direction
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            curr_row += 1 if going_down else -1

        # Join all rows
        return ''.join(rows)