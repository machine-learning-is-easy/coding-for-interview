

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        q = deque([([], -1)])
        res = 0

        while q:
            cur, idx = q.popleft()
            res += 1

            for i in range(idx + 1, len(nums)):
                if nums[i] - k in cur or nums[i] + k in cur:
                    continue
                q.append((cur + [nums[i]], i))

        return res - 1
