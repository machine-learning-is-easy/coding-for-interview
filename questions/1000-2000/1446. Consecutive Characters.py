

class Solution:
    def maxPower(self, s: str) -> int:

        prev = ""
        count = 0
        maximum = 0
        for l in s:
            if l == prev:
                count += 1
            else:
                count = 1
                prev = l
            maximum = max(maximum, count)
        return maximum