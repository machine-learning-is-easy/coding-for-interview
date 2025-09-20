


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Get the length of the two numbers
        l1, l2 = len(num1), len(num2)
        # Make sure that string1 is always smaller
        if l1 > l2:
            num1, num2 = num2, num1
            l1, l2 = l2, l1

        # convert longer string to an integer value
        n2, pow_ = 0, 1

        for ch in num2[::-1]:
            n2 += (ord(ch) - ord('0')) * pow_
            pow_ *= 10

        pow_, retval = 1, 0

        # Go over each character in the smaller number from back and accumulate answer
        for ch in num1[::-1]:
            chdgt = ord(ch) - ord('0')
            curr = 0
            while chdgt > 0:
                curr += n2
                chdgt -= 1

            retval += pow_ * curr
            pow_ *= 10

        return str(retval)


"""
Input: num1 = "123", num2 = "456"
Output: "56088"
"""

num1 = "123"
num2 = "456"

assert Solution().multiply(num1, num2) == "56088"


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1_list = list(num1)[::-1]
        num2_list = list(num2)[::-1]
        for idx1 in range(len(num1_list)):
            for idx2 in range(len(num2_list)):
                digit_res = int(num1_list[idx1]) * int(num2_list[idx2])
                res[idx1 + idx2] += digit_res # need to add existing value than apply // 10 and %10
                res[idx1 + idx2 + 1] += res[idx1 + idx2] // 10
                res[idx1 + idx2] = res[idx1 + idx2] % 10

        while res and res[-1] == 0:
            res.pop(-1)
        res = [str(i) for i in res]

        return "".join(res[::-1])
