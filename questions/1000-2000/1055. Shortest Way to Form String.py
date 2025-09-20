


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        for t in target:
            if not t in source:
                return -1

        result = 1
        i, j = 0, 0

        while i < len(target):
            if j >= len(source):
                j = 0
                result += 1
            if target[i] == source[j]:
                i += 1
            j += 1

        return result