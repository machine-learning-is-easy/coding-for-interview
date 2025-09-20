

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber:
            # there is no A0 in the expression, need to minus 1, to gurantee there is some value
            # in the lowest priority digit
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            ans = chr(65 + remainder) + ans
        return ans