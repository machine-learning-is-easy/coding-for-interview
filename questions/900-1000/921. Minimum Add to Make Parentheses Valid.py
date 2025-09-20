

class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []  # stack to recieve letter in s

        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if stack:
                    if stack[-1] == "(":
                        stack.pop(-1)
                    else:
                        stack.append(c)
                else:
                    stack.append(c)

        return len(stack)