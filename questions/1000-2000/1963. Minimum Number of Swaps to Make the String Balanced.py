

# the best swap is orphan bracket //2 then ceil(/2)
class Solution:
    def minSwaps(self, s: str) -> int:

        stack = []
        for p in s:
            if p == "[":
                stack.append(p)
            else:
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(p)

        orphan = len(stack) // 2
        return ceil(orphan / 2)
