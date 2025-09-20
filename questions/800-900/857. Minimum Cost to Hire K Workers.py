
import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, K: int) -> float:
        # ********* worth to look back
        from fractions import Fraction
        # sort the ratio from lower to highest
        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))

        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            # iteration list from lower ratio to high ratio
            # record total quality
            heapq.heappush(pool, -q)
            # record total quality
            sumq += q

            if len(pool) > K:
                # pop higher quality
                # if the ratio is the same, will pop higher quality person. it will save sum cost
                # if higher quality has lower ratio. will pop higher quality person
                # because ratio is increasing, need to drop higher quality person and test higher
                # but lower quality cost
                sumq += heapq.heappop(pool)

            if len(pool) == K:
                # current ratio is the highest ratio. it must to meet the lower ratio person
                # using higher ratio to pay K, total_quality (propotional to quality)
                # iteration this process and record the lowerest cost
                ans = min(ans, ratio * sumq)

        return float(ans)

quality = [10,20,5]
wage = [70,50,30]
k = 2

assert Solution().mincostToHireWorkers(quality, wage, k)== 105