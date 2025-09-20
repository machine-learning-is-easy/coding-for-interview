
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # binary search
        candidate = str1 if len(str1) < len(str2) else str2
        while candidate:
            str1_divide = str1 == candidate * (len(str1) // len(candidate))
            str2_divide = str2 == candidate * (len(str2) // len(candidate))
            if (not str1_divide) or (not str2_divide):
                candidate = candidate[:(len(candidate) // 2)]
            else:
                return candidate
        return ''