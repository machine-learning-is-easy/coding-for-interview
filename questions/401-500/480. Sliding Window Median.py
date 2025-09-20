

from collections import defaultdict
from heapq import heappop, heappush, heapify
class Solution:
    # TC - O((n - k)*log(k))
    # SC - O(k)
    # 121 ms, faster than 96.23%

    def find_median(self, max_heap, min_heap, heap_size):
        if heap_size % 2 == 1:
            return -max_heap[0]
        else:
            return (-max_heap[0] + min_heap[0]) / 2

    def medianSlidingWindow(self, nums, k: int):
        max_heap = []
        min_heap = []
        heap_dict = defaultdict(int)
        result = []

        for i in range(k):
            heappush(max_heap, -nums[i])
            heappush(min_heap, -heappop(max_heap))
            if len(min_heap) > len(max_heap):
                heappush(max_heap, -heappop(min_heap))

        median = self.find_median(max_heap, min_heap, k)
        result.append(median)

        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            heap_dict[prev_num] += 1

            balance = -1 if prev_num <= median else 1

            if nums[i] <= median:
                balance += 1
                heappush(max_heap, -nums[i])
            else:
                balance -= 1
                heappush(min_heap, nums[i])

            if balance < 0:
                heappush(max_heap, -heappop(min_heap))
            elif balance > 0:
                heappush(min_heap, -heappop(max_heap))

            # only pop the first element which are not in the K interval.
            while max_heap and heap_dict[-max_heap[0]] > 0:
                heap_dict[-max_heap[0]] -= 1
                heappop(max_heap)

            while min_heap and heap_dict[min_heap[0]] > 0:
                heap_dict[min_heap[0]] -= 1
                heappop(min_heap)

            median = self.find_median(max_heap, min_heap, k)
            result.append(median)

        return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3

assert Solution().medianSlidingWindow(nums=nums, k=k) == [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]


# simple solution

class Solution:
    # TC - O((n - k)*log(k))
    # SC - O(k)
    # 121 ms, faster than 96.23%

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList()
        result = []

        for i in range(len(nums)):
            window.add(nums[i])
            if i >= k:
                window.remove(nums[i - k])

            if i >= k - 1:
                if k % 2 == 1:
                    result.append(float(window[k // 2]))
                else:
                    result.append((window[k // 2 - 1] + window[k // 2]) / 2)

        return result