
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                v = stack.pop(-1)
                stack[-1] += max(2 * v, 1)
        return stack.pop(-1)