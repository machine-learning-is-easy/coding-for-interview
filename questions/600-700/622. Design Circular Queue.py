
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k  # initialize a list of size k
        self.capacity = k     # maximum size of the queue
        self.size = 0         # current number of elements
        self.front = 0        # index of the front element
        self.rear = -1        # index of the last element

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity  # circular increment
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity  # circular increment
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity