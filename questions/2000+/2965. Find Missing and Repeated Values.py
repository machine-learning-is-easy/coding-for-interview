

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_numbers = n * n
        expected_sum = total_numbers * (total_numbers + 1) // 2

        actual_sum = actual_sq_sum = 0
        num_counts = {}

        for row in grid:
            for num in row:
                actual_sum += num
                num_counts[num] = num_counts.get(num, 0) + 1

        a = b = 0
        for num, count in num_counts.items():
            if count == 2:
                a = num  # The repeated number
                break

        b = a + (expected_sum - actual_sum)

        return [a, b]