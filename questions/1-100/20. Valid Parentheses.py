
class Solution:
    def isValid(self, s: str) -> bool:
        # stack to add and pop
        stack = []
        for c in s:
            if c in [")", "]", "}"]:
                if len(stack) == 0:
                    return False

                elif c == ")":
                    if stack[-1] != "(":
                        return False
                    else:
                        stack.pop()
                elif c == "]":
                    if stack[-1] != "[":
                        return False
                    else:
                        stack.pop()
                elif c == "}":
                    if stack[-1] != "{":
                        return False
                    else:
                        stack.pop()

            elif c in ["(", "[", "{"]:
                stack.append(c)
            else:
                raise Exception("Not allowed {}".format(c))
        if len(stack) > 0:
            return False
        else:
            return True