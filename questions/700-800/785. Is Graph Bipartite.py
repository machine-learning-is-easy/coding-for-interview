

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        hashmap = {}  # we need to add value to the key, so it is a dict. normally, if only record visited hash table,
        # we can use set instead of dict.
        for node in range(len(graph)):
            if node not in hashmap:
                stack = [node]
                hashmap[node] = 0  # works, because it is fully connect to other connection nodes except itself.
                # if the given graph is not fully connected with other nodes or undirectly connected. we should convert
                # it to bidirectionaly graph
                while stack:  # breath first search
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in hashmap:
                            stack.append(nei)
                            hashmap[nei] = hashmap[node] ^ 1 # 0 to 1 or 1 to 0
                        elif hashmap[nei] == hashmap[node]:
                            return False
        return True