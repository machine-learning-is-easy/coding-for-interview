


class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return "0"

        stack, num, sign = [], 0, "+"

        for i in range(len(s)):

            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord("0")

            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if sign == "-":
                    stack.append(-num)

                elif sign == "+":
                    stack.append(num)

                elif sign == "*":
                    stack.append(stack.pop() * num)

                else:  # sign == "/"
                    tmp = stack.pop()
                    tmp = abs(tmp) // num if tmp >= 0 else -(abs(tmp) // num)
                    stack.append(tmp)

                sign = s[i]
                num = 0

        return sum(stack)


# another solution
class Solution:
    def calculate(self, s: str) -> int:

        num_stack = []
        operator_stack = ["+"]

        ind = 0
        while ind < len(s):

            if s[ind] == " ":
                ind += 1
            elif s[ind] in ["+", "-", "*", "/"]:
                operator_stack.append(s[ind])
                ind += 1
            else:
                k = ind
                while k < len(s) and s[k].isdigit():
                    k += 1

                num = int(s[ind:k])
                ind = k

                if operator_stack[-1] == "+":
                    num_stack.append(num)
                elif operator_stack[-1] == "-":
                    num_stack.append(-num)
                elif operator_stack[-1] == "*":
                    num_stack.append(num_stack.pop(-1) * num)
                elif operator_stack[-1] == "/":
                    if num != 0:
                        if num_stack[-1] > 0:
                            num_stack.append(floor(num_stack.pop(-1) / num))
                        else:
                            num_stack.append(ceil(num_stack.pop(-1) / num))
                    else:
                        raise Exception("Divide by 0")
                else:
                    raise Exception("Operator is not support")

        return sum(num_stack)