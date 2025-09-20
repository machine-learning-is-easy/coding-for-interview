
class Solution:
    def appealSum(self, s: str) -> int:

        def get_len(s):
            c_hash = set()
            for c in s:
                c_hash.add(c)
            print(s, print(len(c_hash)))

            return len(c_hash)

        total_len = 0
        s_len = len(s)
        for ind in range(s_len):
            for ind1 in range(ind + 1, s_len):
                total_len += get_len(s[ind:ind1])

        return total_len

assert Solution().appealSum("abbca") == 28