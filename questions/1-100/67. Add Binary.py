


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        carry = 0
        pa = len(a) - 1
        pb = len(b) - 1
        res = []
        while pa >= 0 or pb >= 0:
            va = ord(a[pa]) - ord("0") if pa >= 0 else 0
            vb = ord(b[pb]) - ord("0") if pb >= 0 else 0

            vc = (va + vb + carry) % 2
            carry = (va + vb + carry) // 2
            res.append(str(vc))
            pa -= 1
            pb -= 1
        if carry:
            res.append(str(carry))
        return "".join(res[::-1])
