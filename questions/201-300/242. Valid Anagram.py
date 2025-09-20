
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # convert two string into hashmap, then compare two hash table

        s_hm = defaultdict(int)
        for s_ind in s:
            s_hm[s_ind] += 1

        t_hm = defaultdict(int)
        for t_ind in t:
            t_hm[t_ind] += 1

        if s_hm == t_hm:
            return True
        else:
            return False
