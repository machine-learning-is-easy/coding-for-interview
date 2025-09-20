
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        p_stack = []

        for ind, p in enumerate(s):
            if p == "(":
                p_stack.append(ind)
            else:
                if p_stack and s[p_stack[-1]] == "(":
                    p_stack.pop(-1)
                elif p_stack and s[p_stack[-1]] == ")" and (locked[ind] == "0" or locked[p_stack[-1]] == "0"):
                    p_stack.pop(-1)
                else:
                    p_stack.append(ind)

        if p_stack:
            return False
        else:
            return True