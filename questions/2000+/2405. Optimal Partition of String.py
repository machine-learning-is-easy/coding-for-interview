

class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        t = 1
        for c in s:
            if c in seen:
                t += 1
                seen = {c}
            else:
                seen.add(c)
        return t