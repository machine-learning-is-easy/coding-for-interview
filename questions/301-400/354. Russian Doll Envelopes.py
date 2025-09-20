

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Step 1: Sort envelopes
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Step 2: Extract heights
        heights = [h for w, h in envelopes]

        # Step 3: Apply Longest Increasing Subsequence (LIS) on heights
        dp = []
        for h in heights:
            i = bisect_left(dp, h)
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h

        return len(dp)