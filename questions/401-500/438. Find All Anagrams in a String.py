

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []
        # put p into a hash table
        p_h = {}

        for ind, c in enumerate(p):
            if c in p_h:
                p_h[c] += 1
            else:
                p_h[c] = 1

        window_length = len(p)

        def add_dict(hash_table, value):
            if value in hash_table:
                hash_table[value] += 1
            else:
                hash_table[value] = 1

        def deduct_dict(hash_table, value):
            if value in hash_table:
                hash_table[value] -= 1

            if hash_table[value] == 0:
                del hash_table[value]

        res = []
        hash_table = {}
        start = 0
        while start < len(s):
            if start < window_length:
                # put current character in hash table
                add_dict(hash_table, s[start])
            else:
                # pop the start - window_lenght + 1
                deduct_dict(hash_table, s[start - window_length])
                # add the start character
                add_dict(hash_table, s[start])

            if hash_table == p_h:
                res.append(start - window_length + 1)
            start += 1
        return res