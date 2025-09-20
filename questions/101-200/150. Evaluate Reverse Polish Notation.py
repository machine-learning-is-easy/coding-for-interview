

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                a = stack.pop(-1)
                b = stack.pop(-1)
                if token == "+":
                    result = b + a
                elif token == "-":
                    result = b - a
                elif token == "*":
                    result = b * a
                else:
                    result = int(b / a)
                stack.append(result)

            else:
                stack.append(int(token))

        return stack.pop(0)