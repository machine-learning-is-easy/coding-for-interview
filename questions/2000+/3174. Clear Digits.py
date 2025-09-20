

class Solution:
    def clearDigits(self, s: str) -> str:
        start = 0
        res = []
        while start < len(s):
            if s[start].isdigit():
                if len(res) > 0:
                    res.pop(-1)
            else:
                res.append(s[start])
            start += 1

        return "".join(res)