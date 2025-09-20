
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for ind, c in enumerate(s):
            if c == "(":
                stack.append((c, ind))
            elif c == ")":
                if stack:
                    if stack[-1][0] == "(":
                        stack.pop(-1)
                        continue
                stack.append((c, ind))
        s_list = list(s)
        for ind in range(len(stack) - 1, -1, -1):
            s_list[stack[ind][1]] = ''
        return ''.join(s_list)