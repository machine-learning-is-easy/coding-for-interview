

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat
        else:
            res = [[0 for _ in range(c)] for _ in range(r)]

            ind = 0  # index of res matrix

            for row in range(rows):
                for col in range(cols):
                    res[ind // c][ind % c] = mat[row][col]
                    ind += 1

            return res