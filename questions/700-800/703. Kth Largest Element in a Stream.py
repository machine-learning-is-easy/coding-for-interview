

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)  # Convert list to a heap
        # Keep only the k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)  # Add the new value
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)  # Remove smallest if heap exceeds k
        return self.heap[0]  # The kth largest (min of top k)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)