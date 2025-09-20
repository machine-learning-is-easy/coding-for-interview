

class MinStack:

    def __init__(self):
        # Stack to store all elements
        self.stack = []
        # Stack to store the current minimums
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the smaller value between the new val and the current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # If the popped value is the current minimum, pop from min_stack as well
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]