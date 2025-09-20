

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        def prefix(str1, str2):
            length = 0
            for a, b in zip(str1, str2):
                if a == b:
                    length += 1
                else:
                    break
            return length

        max_prefix = 0
        for d1 in arr1:
            str1 = str(d1)
            for d2 in arr2:
                str2 = str(d2)
                leng = prefix(str1, str2)
                max_prefix = max(max_prefix, leng)
        return max_prefix