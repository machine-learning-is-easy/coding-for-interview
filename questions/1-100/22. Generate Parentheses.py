

class Solution:
    def generateParenthesis(self, n: int):

        stack = []
        res = []

        def backtracking(tmp, step):
            nonlocal stack
            if step >= n * 2:
                if stack == []:
                    res.append(''.join(tmp))
                return
            else:
                if stack == []:
                    tmp.append("(")
                    stack.append(")")
                    backtracking(tmp, step + 1)
                    tmp.pop(-1)
                    stack.pop(-1)
                else:
                    s = stack.pop(-1)
                    tmp.append(s)
                    backtracking(tmp, step + 1)
                    tmp.pop(-1)
                    stack.append(s)

                    tmp.append("(")
                    stack.append(")")
                    backtracking(tmp, step + 1)
                    tmp.pop(-1)
                    stack.pop(-1)

        backtracking([], 0)
        return res


n = 3
assert Solution().generateParenthesis(n) == ["((()))","(()())","(())()","()(())","()()()"]

#the time complexity is nth catalan number