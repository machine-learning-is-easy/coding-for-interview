

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num

        while l <= r:
            mid = (l + r) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                l = mid + 1
            elif square > num:
                r = mid - 1
        return False