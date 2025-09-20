

class Solution:
    def partitionLabels(self, S: str):
        last = {c: i for i, c in enumerate(S)}
        # j record all visited letter maximum index
        # anchor record the begining index
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans

s = "eccbbbbdec"

assert Solution().partitionLabels(s) == [10]