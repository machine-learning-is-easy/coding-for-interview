

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        def bs(row):
            beg = 0
            end = cols-1

            while beg<=end:
                mid = (beg+end)//2
                if binaryMatrix.get(row, mid)==1:
                    end = mid-1
                else:
                    beg = mid+1
            return beg

        ans = float('inf')
        rows, cols = binaryMatrix.dimensions()
        for row in range(rows):
            ans = min(ans, bs(row))
        if ans == cols:
            return -1
        return ans