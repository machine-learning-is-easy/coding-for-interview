

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def check(arr, guess, k):
            total = 0
            count = 1
            for i in arr:
                if total + i > guess:
                    total = 0
                    count += 1
                total += i
            return count > k

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2
            if check(nums, mid, k):
                left = mid + 1
            else:
                right = mid

        return left

# time complexity is nlogS
# brutal force solution is DFS
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        @lru_cache(None)
        def dfs(start, k):
            if k == 1:
                return sum(nums[start:])  # O(n) worst case here

            min_largest = float('inf')
            current_sum = 0

            for i in range(start, len(nums) - k + 1):  # i goes from start to n-k
                current_sum += nums[i]  # O(1)
                largest = max(current_sum, dfs(i + 1, k - 1))  # recursion
                min_largest = min(min_largest, largest)
                if current_sum > min_largest:
                    break  # pruning (helps in practice, not worst-case)

            return min_largest

        return dfs(0, k)