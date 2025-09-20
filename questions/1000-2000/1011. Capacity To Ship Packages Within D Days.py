


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)
        while lo <= hi:
            mid = (lo + hi) // 2
            if not self.is_possible(weights, days, mid):
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

    def is_possible(self, weights, days, size):
        t = 0
        for w in weights:
            t += w
            if t > size:
                # if greater than size, days - 1, remain days deduct 1, t = w starting new calculation
                days -= 1
                t = w
                if days == 0:  # if days == 0. means not possible.
                    break
        return days > 0 # all the days are not consumed, if True, it is possible.


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_deliver(arr, days, capacity):
            count = 0
            idx = 0
            subcount = 0
            while idx < len(arr):
                elif subcount + arr[idx] > capacity:
                    count += 1
                    subcount = arr[idx]
                    if subcount > capacity:
                        return False
                else:
                    subcount += arr[idx]
                idx += 1
            if subcount > 0:
                count += 1
            return count <= days
        l = 0
        r = sum(weights)
        while l <= r:
            mid = (l + r) // 2
            if can_deliver(weights, days, mid) is True:
                r = mid - 1
            else:
                l = mid + 1
        return l