


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        p1, p2 = 0, 0

        res = ""
        signal = 0
        while p1 < len(word1) and p2 < len(word2):
            if signal == 0:
                res += word1[p1]
                p1 += 1
                signal = 1
            elif signal == 1:
                res += word2[p2]
                p2 += 1
                signal = 0

        if p1 < len(word1):
            res += word1[p1:]
        if p2 < len(word2):
            res += word2[p2:]

        return res