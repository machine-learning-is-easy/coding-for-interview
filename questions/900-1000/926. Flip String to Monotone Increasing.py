


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        left_1 = [0] * len(s)
        right_0 = [0] * len(s)

        count = 0
        for ind, c in enumerate(s):
            if c == '1':
                count += 1
            left_1[ind] = count

        count = 0
        for ind in range(len(s) - 1, -1, -1):
            right_0[ind] = count
            if s[ind] == '0':
                count += 1

        res = math.inf
        ind = 0

        while ind < len(left_1):
            res = min(res, left_1[ind] + right_0[ind])
            ind += 1

        return min(res, max(left_1), max(right_0))

