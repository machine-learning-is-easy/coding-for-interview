

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        ans = []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            ans.append(current)

            for next_course in adj[current]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return len(ans) == n

# try to use dictionary to store the indegree and adj
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        res = []

        for dependent in prerequisites:
            course, req = dependent
            indegree[course] += 1
            adj[req].append(course)

        queue = []
        print(indegree)
        for idx in range(numCourses):  # this is different
            if indegree.get(idx, 0) == 0:
                queue.append(idx)

        while queue:
            course = queue.pop(0)
            res.append(course)
            for nxt in adj.get(course, []):
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
            print(queue)
        return len(res) == numCourses