
# question: n is positive or negative
# if the n can be negative
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        current_product = x
        current_pow = n

        while current_pow > 0:
            if current_pow % 2 == 1:
                ans *= current_product
            current_product *= current_product
            current_pow = current_pow // 2
        return ans

assert Solution().myPow(2, 10) == 1024