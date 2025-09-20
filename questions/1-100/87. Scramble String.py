


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def func(s1, s2):
            if not sorted(s1) == sorted(s2):
                return False
            if len(s1) == 1:
                return True
            for i in range(1, len(s1)):
                if (func(s1[:i], s2[-i:]) and func(s1[i:], s2[:-i])) or (func(s1[:i], s2[:i]) and func(s1[i:], s2[i:])):
                    return True
            return False
        return func(s1, s2)