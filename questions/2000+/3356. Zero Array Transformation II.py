
# key point is to use difference array to simulate the process of queries
# becareful about the index of difference array

# does not pass all test cases
class Solution:
    def minZeroArray(self, nums, queries) -> int:
        n = len(nums)
        def canMakeZero(k: int) -> bool:
            temp = nums[:]  # Copy nums for simulation
            diff = [0] * (n + 1)  # Difference array for range updates

            for i in range(k):
                l, r, val = queries[i]
                diff[l] -= val
                diff[r + 1] += val

            curr = 0
            for i in range(n):
                curr += diff[i]
                temp[i] += curr  # Apply accumulated decrement
                if temp[i] > 0:  # If any value is still positive, return False
                    return False
            return True

        left, right = 1, len(queries) + 1
        while left < right:
            mid = (left + right) // 2
            if canMakeZero(mid):
                right = mid
            else:
                left = mid + 1

        return left if left <= len(queries) else -1

# works solution below
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        left, right = 0, len(queries)

        # Zero array isn't formed after all queries are processed
        if not self.can_form_zero_array(nums, queries, right):
            return -1

        # Binary Search
        while left <= right:
            middle = left + (right - left) // 2
            if self.can_form_zero_array(nums, queries, middle):
                right = middle - 1
            else:
                left = middle + 1

        # Return earliest query that zero array can be formed
        return left

    def can_form_zero_array(
        self, nums: List[int], queries: List[List[int]], k: int
    ) -> bool:
        n = len(nums)
        total_sum = 0
        difference_array = [0] * (n + 1)

        # Process query
        for query_index in range(k):
            start, end, val = queries[query_index]

            # Process start and end of range
            difference_array[start] += val
            difference_array[end + 1] -= val

        # Check if zero array can be formed
        for num_index in range(n):
            total_sum += difference_array[num_index]
            if total_sum < nums[num_index]:
                return False
        return True


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def isPossible(k):
            diff = [0] * (len(nums) + 1)
            for idx in range(k + 1):
                start, end, v = queries[idx]
                diff[start] -= v
                diff[end + 1] += v
            acc_diff = 0
            for idx, num in enumerate(nums):
                acc_diff += diff[idx]
                if acc_diff + num > 0:
                    return False
            return True

        left, right = -1, len(queries) - 1
        while left <= right:
            mid = (left + right) // 2
            if isPossible(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left + 1 if left < len(queries) else -1

nums = [2,0,2]
queries = [[0,2,1],[0,2,1],[1,1,3]]

assert Solution().minZeroArray(nums, queries) == -1