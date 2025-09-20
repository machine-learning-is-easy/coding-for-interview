

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def can_assign(k):
            # Take the k strongest workers and keep them in a sorted list
            avail = workers[-k:]
            pills_left = pills

            # Try to assign the k hardest tasks (i = k-1 down to 0)
            for i in range(k - 1, -1, -1):
                need = tasks[i]
                # If the strongest worker can do it without a pill:
                if avail and avail[-1] >= need:
                    avail.pop()  # use that worker
                else:
                    # Need a pill: find the smallest worker w with w + strength >= need
                    target = need - strength
                    idx = bisect.bisect_left(avail, target)
                    if idx == len(avail):  # no worker can even with pill
                        return False
                    # use that worker with a pill
                    avail.pop(idx)
                    pills_left -= 1
                    if pills_left < 0:
                        return False
            return True

        # Binary search on the number of tasks
        left, right = 0, min(len(tasks), len(workers))
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans