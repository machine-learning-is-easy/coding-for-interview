

# questions: need to check if there can be more than 2 duplicates in the string, if so, this solution will not work
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for c in s:
            if res:
                if res[-1] == c:
                    res.pop(-1)
                else:
                    res.append(c)
            else:
                res.append(c)
        return ''.join(res)