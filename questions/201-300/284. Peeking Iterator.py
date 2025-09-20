

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.buffer = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.buffer

    def next(self):
        """
        :rtype: int
        """
        next = self.buffer
        self.buffer = self.iterator.next() if self.iterator.hasNext() else None
        return next

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.buffer is not None