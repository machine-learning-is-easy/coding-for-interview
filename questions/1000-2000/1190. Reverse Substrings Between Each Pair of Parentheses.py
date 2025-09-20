

class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = []
        for c in s:
            if c == ")":
                # pop up the stack until "("
                sub_string = ''
                while stack[-1] != "(":
                    sub_string += stack.pop(-1)

                stack.pop(-1)
                for sub_c in sub_string:
                    stack.append(sub_c)

            else:
                stack.append(c)

        return ''.join(stack)

s = "(u(love)i)"
assert Solution().reverseParentheses(s) == "iloveu"