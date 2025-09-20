
"""
tips using sorting the original string. and iteration over s2, sorting the substring starting with index and length of s1. if sorted original string is the same with sorted subarray. return True. 
"""

"""
the same with anagrams.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        count1 = Counter(s1)
        count2 = Counter(s2[:len1])

        if count1 == count2:
            return True

        for i in range(len1, len2):
            count2[s2[i]] += 1
            count2[s2[i - len1]] -= 1
            if count2[s2[i - len1]] == 0:
                del count2[s2[i - len1]]
            if count1 == count2:
                return True

        return False