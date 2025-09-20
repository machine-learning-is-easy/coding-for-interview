

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for ind in range(int(len(s)/2)):
            tmp = s[ind]
            s[ind] = s[length - 1 - ind]
            s[length - 1 - ind] = tmp