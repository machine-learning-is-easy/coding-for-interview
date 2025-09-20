

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        if sign == -1:
            x = x * -1

        rev = 0
        while x:
            rev = rev * 10 + x % 10
            x = x // 10

        rev = sign * rev

        if rev > 2 ** 31 - 1 or rev < -2 ** 31:
            return 0
        else:
            return rev

