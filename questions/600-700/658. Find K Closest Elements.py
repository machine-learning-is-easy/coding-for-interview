

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l, r = 0, len(arr)

        while l < r:
            mid = (l + r) // 2

            if mid + k < len(arr):
                if x - arr[mid] > arr[mid + k] - x:  # mid + 1 : mid + k is lower
                    l = mid + 1
                else:  # mid + 1 : mid + k is lower
                    r = mid
            else:
                r = r - 1

        return arr[l:l + k]


class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if mid + k >= len(arr):
                r = r - 1
            continue

            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid - 1
        return arr[l: l + k]


arr = [1,2,3,4,5]
k = 4
x = 3
