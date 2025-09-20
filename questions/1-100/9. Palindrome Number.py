"""
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)

        total_l = len(str_x)

        for digit in range(total_l // 2):
            if str_x[digit] != str_x[total_l - 1 - digit]:
                return False

        return True