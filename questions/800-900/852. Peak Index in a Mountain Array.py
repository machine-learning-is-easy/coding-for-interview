

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:  # Peak is on the right side
                left = mid + 1
            else:  # Peak is on the left side or at mid
                right = mid

        return left