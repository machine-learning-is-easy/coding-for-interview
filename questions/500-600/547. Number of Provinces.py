

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        # conver to a dict

        connection_dict = defaultdict(list)

        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c] == 1:
                    connection_dict[r].append(c)
                    connection_dict[c].append(r)

        visited = set()

        number = 0

        def dfs(key):
            if key in connection_dict:
                visited.add(key) # current process
                # dfs searching neighbours
                for elem in connection_dict[key]:
                    if elem in connection_dict and elem not in visited:
                        dfs(elem)

        for key in connection_dict.keys():
            if key not in visited:
                number += 1
            dfs(key)
        return number

