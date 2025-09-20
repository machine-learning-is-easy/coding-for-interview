

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def checkSimilar(ref, test):
            diff = []
            for i in range(len(ref)):
                if ref[i] != test[i]:
                    diff.append(i)
                    if len(diff) > 2:
                        return False
            if len(diff) == 2:
                test[diff[0]], test[diff[1]] = test[diff[1]], test[diff[0]]
            return test == ref

        def bfs(same_group):

            for ref in same_group:
                # we continue expand same_group size until none of string in self.strs is similar to strings in
                # same_groups, when same group size changes, ref continue to get the extra element.
                idx = 0
                while idx < len(self.strs):
                    # this need to check if idx < len(self.strs), self.strs length is changing
                    if ref == self.strs[idx] or checkSimilar(list(ref), list(self.strs[idx])):  # same or similar
                        same_group.append(self.strs.pop(idx))
                        # self.strs size changes and same_group size changes as well
                        # the idx should not increase
                    else:
                        idx += 1
            return same_group

        self.strs = strs[:]
        groups = list()
        while self.strs:  # continue searching similar until all string are clustered, until empty list
            groups.append(bfs([self.strs.pop()]))

        return len(groups)


# another version with faster
class Solution:
    def compare(self, s1, s2):
        N = len(s1)
        idx1 = -1
        idx2 = -1
        for i in range(N):
            ch1, ch2 = s1[i], s2[i]
            if ch1 != ch2:
                if idx1 == -1:
                    idx1 = i
                elif idx2 == -1:
                    idx2 = i
                else:
                    return False

        if idx1 == -1:
            return True

        if idx2 == -1:
            return False

        return s1[idx1] == s2[idx2] and s1[idx2] == s2[idx1]

    def numSimilarGroups(self, strs: List[str]) -> int:
        N = len(strs)
        graph = [[] for _ in range(N)]
        for i in range(N):
            for j in range(i+1, N):
                if self.compare(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [False for _ in range(N)]
        ans = 0
        for i in range(N):
            if visited[i]:
                continue
            ans += 1
            q = deque([i])
            while len(q) > 0:
                u = q.popleft()
                if visited[u]:
                    continue
                visited[u] = True
                for v in graph[u]:
                    if visited[v]:
                        continue
                    q.append(v)

        return ans
