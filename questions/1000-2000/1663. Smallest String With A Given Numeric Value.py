

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = [0] * n
        for position in range(n - 1, -1, -1):
            add = min(k - position, 26)
            result[position] = chr(ord("a") + add - 1)
            k -= add

        return "".join(result)