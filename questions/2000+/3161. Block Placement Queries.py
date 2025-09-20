

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        obstacles = SortedList()
        results = []

        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])
            else:
                x, sz = q[1], q[2]
                can_place = False
                prev = 0

                # Consider obstacles within [0, x]
                idx = obstacles.bisect_right(x)
                for i in range(idx):
                    curr = obstacles[i]
                    if curr - prev >= sz:
                        can_place = True
                        break
                    prev = curr + 1  # Next possible position after obstacle

                # Check space after last obstacle to x
                if not can_place and x - prev + 1 >= sz:
                    can_place = True

                results.append(can_place)

        return results