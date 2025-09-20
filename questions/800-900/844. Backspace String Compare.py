

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def back_string(s):
            tmp = s[::-1]
            s_ret = ''
            skip_stack = []
            for c in tmp:
                if c == "#":
                    skip_stack.append(1)
                else:
                    if len(skip_stack) > 0:
                        skip_stack.pop()
                    else:
                        s_ret += c

            return s_ret[::-1]

        return back_string(S) == back_string(T)