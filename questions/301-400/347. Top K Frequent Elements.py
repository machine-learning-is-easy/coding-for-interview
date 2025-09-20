

from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time
        if k == len(nums):
            return nums

        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)

# O(nlogn)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [x[0] for x in count.most_common(k)]

# use binary heap to get the k most frequent elements
# O(nlogk)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = [(-value, key) for key, value in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = collections.Counter(nums)
        heap_list = []
        for key, value in nums_dict.items():
            if len(heap_list) < k:
                heappush(heap_list, (value, key))
            else:
                if value > heap_list[0][0]:
                    heappush(heap_list, (value, key))
                    heappop(heap_list)

        return [key for value, key in heap_list]

# O(nlogn)