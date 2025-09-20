
class Solution:
    def minOperations(self, logs: List[str]) -> int:

        stack = []
        for lg in logs:
            if lg != './':
                if lg != '../':
                    stack.append(lg)
                else:
                    if stack:
                        stack.pop()
        return len(stack)