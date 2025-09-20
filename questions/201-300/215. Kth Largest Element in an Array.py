

class Solution():
    def findKthLargest(self, nums, k: int) -> int:
        n = len(nums)
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[i] < arr[left]:
                largest = left

            if right < n and arr[largest] < arr[right]:
                largest = right

            if largest != i:
                arr[largest], arr[i] = arr[i], arr[largest]
                heapify(arr, n, largest)

        # convert the list into largest heap
        for i in range(len(nums) // 2, -1, -1):
            heapify(nums, n, i)

        for i in range(k):
            nums[0], nums[n - 1 - i] = nums[n - 1 - i], nums[0]
            heapify(nums, n - i - 1, 0)

        return nums[-k]



    # Driver Code
# print(Solution().findKthLargest([3,2,1,5,6,4], 2)) == 5
# assert Solution().findKthLargest([2, 1], 2) ==
# assert Solution().findKthLargest([-1,-1], 2) == -1
assert Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4

from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            if h:
                num > h[0]
                heappush(h, num)
                if len(h) > k:
                    heappop(h)
            else:
                h.append(num)

        return h[0]