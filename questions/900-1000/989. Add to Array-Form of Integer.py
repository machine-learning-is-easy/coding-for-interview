

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        i = len(num) - 1
        carry = k

        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]
                i -= 1
            res.append(carry % 10)
            carry //= 10

        return res[::-1]  # Reverse to get the correct order


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        carry = k

        idx = len(num) - 1
        while idx >= 0:
            n = num[idx]
            v = carry % 10
            res.append((n + v) % 10)
            carry = carry // 10
            carry += (n + v) // 10
            idx -= 1

        while carry:
            res.append(carry%10)
            carry = carry // 10
        return res[::-1]