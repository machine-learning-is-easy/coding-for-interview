

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.ans = ''

        def backtrack(path):
            nonlocal k
            if k == 0: return
            if len(path) == n:
                k -= 1
                self.ans = "".join(path)
                return
            for i in range(3):
                char = chr(97 + i)
                if not path or path[-1] != char:
                    path.append(char)
                    backtrack(path)
                    path.pop()

        backtrack([])

        return self.ans if not k else ''

# more concised solution
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(curr):
            if len(curr) == n:
                happy_strings.append(curr)
                return
            for ch in 'abc':
                if not curr or curr[-1] != ch:  # Ensure no consecutive characters are the same
                    backtrack(curr + ch)

        happy_strings = []
        backtrack("")

        return happy_strings[k - 1] if k <= len(happy_strings) else ""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        queue = [""]
        while queue:
            cur = queue.pop(0)
            if cur and len(cur) == n:
                res.append(cur)
            if len(res) == k:
                return res[-1]
            if len(cur) >= n:
                continue

            for c in "abc":
                if not cur or cur[-1] != c:
                    queue.append(cur + c)

        return ""