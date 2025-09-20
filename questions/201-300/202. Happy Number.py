
class Solution:
    def isHappy(self, n: int) -> bool:
        def sqnum(n):
            temp = n
            sum = 0
            while temp > 0:
                rem = temp % 10
                sum += rem ** 2
                temp = temp // 10
            return sum

        for i in range(100):
            n = sqnum(n)
            if n == 1:
                return True
        else:
            return False