
from collections import deque, defaultdict
from itertools import groupby

class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        can = {0, firstPerson}
        for _, grp in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            queue = set()
            graph = defaultdict(list)
            for x, y, _ in grp:
                graph[x].append(y)
                graph[y].append(x)
                if x in can: queue.add(x)
                if y in can: queue.add(y)

            queue = deque(queue)
            while queue:
                x = queue.popleft()
                for y in graph[x]:
                    if y not in can:
                        can.add(y)
                        queue.append(y)
        return can

n = 6
meetings = [[1,2,5],[2,3,8],[1,5,10]]
firstperson = 1
assert Solution().findAllPeople(n, meetings, firstperson) == {0,1,2,3,5}
