

# binary search if return the lowest value, return right, if return the highest value, return left
# need to verify if x between 0 and 1
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:
            return x
        else:
            l, r = 1, x

            while l <= r:
                mid = l + (r - l) // 2

                if mid * mid > x:
                    r = mid - 1
                elif mid * mid < x:
                    l = mid + 1
                else:
                    return mid
            else:
                return r