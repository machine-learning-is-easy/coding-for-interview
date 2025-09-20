
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        out = ''
        sign = 1
        for i, c in enumerate(s):
            # print(f's: {s}, c: {c}, out: {out}, sign: {sign}')
            if i == 0 and c in ('+', '-'):
                sign = -1 if c == '-' else 1
            elif c.isdigit():
                out += c
            else:
                break

        out = int(out) * sign if out else 0

        if out > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif out < -2 ** 31:
            return -2 ** 31
        else:
            return out
