

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_table = {}

        for c in s:
            if c in hash_table:
                hash_table[c] += 1
            else:
                hash_table[c] = 1

        for ind, c in enumerate(s):
            if hash_table[c] == 1:
                return ind

        return -1