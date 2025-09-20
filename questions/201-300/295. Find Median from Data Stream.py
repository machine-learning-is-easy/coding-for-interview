
import heapq
from heapq import heappush, heappop, heapify
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num):
        heappush(self.small, -num)
        heappush(self.large, -heappop(self.small))

        if len(self.small) < len(self.large):
            heappush(self.small, -heappop(self.large))

    def findMedian(self):
        if len(self.large) != len(self.small):
            return -self.small[0]
        else:
            return (self.large[0] - self.small[0]) / 2

        # Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()