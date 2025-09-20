

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        # Find indices where characters differ
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)

        # Check if exactly 2 positions differ and can be swapped
        if len(diff) == 2:
            i, j = diff
            return (s1[i] == s2[j] and s1[j] == s2[i])

        return False