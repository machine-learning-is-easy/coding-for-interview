
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        total_pairs = 0
        res = 0
        left = 0

        for right in range(len(nums)):
            x = nums[right]
            total_pairs += freq[x]  # Adding x makes `freq[x]` new pairs
            freq[x] += 1

            # While the window has at least `k` good pairs,
            # count all subarrays starting from current `left`
            while total_pairs >= k:
                res += len(nums) - right
                # Shrink window from left
                freq[nums[left]] -= 1
                total_pairs -= freq[nums[left]]
                left += 1

        return res