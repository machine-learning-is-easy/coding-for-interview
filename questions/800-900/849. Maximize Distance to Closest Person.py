

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        ans = seats.index(1)
        seats.reverse()
        ans = max(ans, seats.index(1))
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K + 1) / 2)

        return int(ans)


# left and right direction
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        l = len(seats)
        left = [0] * l
        right = [0] * l

        anchor = - l
        for ind in range(l):
            if seats[ind] == 1:
                anchor = ind

            left[ind] = ind - anchor

        anchor = 2 * l
        for ind in range(l - 1, -1, -1):
            if seats[ind] == 1:
                anchor = ind
            right[ind] = anchor - ind

        maximum_distance = 0
        for l, r in zip(left, right):
            maximum_distance = max(maximum_distance, min(l, r))

        return maximum_distance
