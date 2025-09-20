

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        result = 0
        sign = 1

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                result += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ")":
                result += sign * num
                result = result * stack.pop(-1)
                result += stack.pop(-1)
                num = 0
        return result + sign * num

# use num_stack and sign_stack, it is better understandable
class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []
        sign_stack = []

        res = 0
        sign = 1  # 1 for '+', -1 for '-'

        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                res += sign * num
                continue  # Skip i += 1 here since we already advanced in the inner loop

            elif char in ['+', '-']:
                sign = 1 if char == "+" else -1
            elif char == '(':
                # Push the result and sign to the stacks
                num_stack.append(res)
                sign_stack.append(sign)
                # Reset for new sub-expression
                res = 0
                sign = 1
            elif char == ')':
                # Pop sign and num from stacks and combine
                res = num_stack.pop() + sign_stack.pop() * res
            # Ignore whitespace
            i += 1

        return res