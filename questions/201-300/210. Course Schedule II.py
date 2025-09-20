

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        G, indegree, ans = defaultdict(list), [0] * numCourses, []
        for nxt, pre in prerequisites:
            G[pre].append(nxt)
            indegree[nxt] += 1

        def dfs(cur):
            ans.append(cur)
            indegree[cur] = -1
            for nextCourse in G[cur]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    dfs(nextCourse)

        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)

        return ans if len(ans) == numCourses else []


# BFS version

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        G = defaultdict(list)
        indegree = [0] * numCourses

        for nxt, pre in prerequisites:
            G[pre].append(nxt)
            indegree[nxt] += 1

        queue = []
        res = []
        for ind in range(len(indegree)):
            if indegree[ind] == 0:
                queue.append(ind)
                res.append(ind)
        while queue:
            c = queue.pop(0)
            for nxt in G[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
                    res.append(nxt)

        return res