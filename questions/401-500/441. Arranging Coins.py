

class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            if mid * (mid + 1) / 2 > n:
                high = mid - 1
            else:
                low = mid + 1
        return high