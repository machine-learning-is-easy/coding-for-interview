
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])

        # Precompute prefix sums for each row
        for row in matrix:
            for c in range(1, cols):
                row[c] += row[c - 1]

        count = 0

        # Fix two columns: left and right
        for left in range(cols):
            for right in range(left, cols):
                sums = defaultdict(int)
                sums[0] = 1
                curr_sum = 0

                for r in range(rows):
                    # Current sum for this row from left to right column
                    row_sum = matrix[r][right]
                    if left > 0:
                        row_sum -= matrix[r][left - 1]

                    curr_sum += row_sum
                    count += sums[curr_sum - target]
                    sums[curr_sum] += 1

        return count