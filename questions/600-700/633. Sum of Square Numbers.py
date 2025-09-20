
from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(sqrt(c))
        while a <= b:
            if c == (a * a) + (b * b):
                return True
            elif c > a * a + b * b:
                a += 1
            else:
                b -= 1
        return False

assert Solution().judgeSquareSum(5) == True