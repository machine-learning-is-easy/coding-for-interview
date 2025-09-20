


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        row1 = len(mat1)
        col1 = len(mat1[0])

        row2 = len(mat2)
        col2 = len(mat2[0])

        res = [[0 for _ in range(col2)] for _ in range(row1)]

        for row in range(row1):
            for col in range(col2):
                ans = 0
                for ind in range(col1):
                    ans += mat1[row][ind] * mat2[ind][col]

                res[row][col] = ans
        return res

# dictionary version, check if the index has value or not
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # put mat1 to dict[row] = {ind: value}
        # put mat2 to dict[col] = {ind: value}
        row1, col1 = len(mat1), len(mat1[0])
        row2, col2 = len(mat2), len(mat2[0])
        mat1_dict = defaultdict(dict)
        mat2_dict = defaultdict(dict)

        for row in range(row1):
            for col in range(col1):
                if mat1[row][col] != 0:
                    mat1_dict[row][col] = mat1[row][col]
        print(mat1_dict)
        for col in range(col2):
            for row in range(row2):
                if mat2[row][col] != 0:
                    mat2_dict[col][row] = mat2[row][col]

        res = [[0 for _ in range(col2)] for _ in range(row1)]
        for row in range(row1):
            for col in range(col2):
                total = 0
                for key in mat1_dict[row]:
                    if key in mat2_dict[col]:
                        total += mat1_dict[row][key] * mat2_dict[col][key]

                res[row][col] = total
        return res