
class MaxStack:

    def __init__(self):
        self.stack = []  # Regular stack
        self.max_heap = []  # Max heap to track max elements
        self.entries = {}  # Dictionary to track valid entries
        self.counter = 0  # Unique counter to track order of elements

    def push(self, x: int) -> None:
        self.stack.append((x, self.counter))
        heapq.heappush(self.max_heap, (-x, -self.counter))
        self.entries[self.counter] = x
        self.counter += 1

    def pop(self) -> int:
        while self.stack:
            x, count = self.stack.pop()
            if count in self.entries:  # Ensure it is not marked as removed
                del self.entries[count]
                return x
        return -1  # Should not happen

    def top(self) -> int:
        while self.stack:
            x, count = self.stack[-1]
            if count in self.entries:
                return x
            self.stack.pop()  # Remove invalidated elements
        return -1  # Should not happen

    def peekMax(self) -> int:
        while self.max_heap:
            x, count = self.max_heap[0]
            if -count in self.entries:  # Ensure it's valid
                return -x
            heapq.heappop(self.max_heap)  # Remove invalidated elements
        return -1  # Should not happen

    def popMax(self) -> int:
        while self.max_heap:
            x, count = heapq.heappop(self.max_heap)
            if -count in self.entries:
                del self.entries[-count]
                # Remove from stack as well
                for i in range(len(self.stack) - 1, -1, -1):
                    if self.stack[i][1] == -count:
                        self.stack.pop(i)
                        break
                return -x
        return -1  # Should not happen

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()