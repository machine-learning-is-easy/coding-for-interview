

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # dimensions of original image
        m, n = len(img), len(img[0])
        # initialize output matrix with zeros
        res = [[0] * n for _ in range(m)]
        # iterate through each cell in the image
        for i in range(m):
            for j in range(n):
                # calculate the sum of the cells in the 3x3 neighborhood
                total = 0
                count = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        # check if the cell is inside the image
                        if 0 <= x < m and 0 <= y < n:
                            total += img[x][y]
                            count += 1
                # calculate the smoothed value for the cell
                res[i][j] = total // count
        return res