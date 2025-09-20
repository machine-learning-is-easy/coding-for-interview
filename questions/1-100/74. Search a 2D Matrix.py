


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # binary search
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False


# two binary search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def BinarySearch(resCol, low, high, target):
            while low <= high:
                mid = (low + high) // 2
                if resCol[mid] == target:
                    return True
                elif resCol[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False

        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                resCol = matrix[mid]
                return BinarySearch(resCol, 0, len(resCol), target)
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False