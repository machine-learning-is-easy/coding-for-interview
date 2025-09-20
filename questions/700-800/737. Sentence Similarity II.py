
from collections import defaultdict

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        graph = defaultdict(list)

        for start, end in similarPairs:
            graph[start].append(end)
            graph[end].append(start)

        sentence1 = set(sentence1)
        sentence2 = set(sentence2)

        def dfs(token):
            if token in sentence1:
                sentence1.remove(token)
                return True
            elif token in graph:
                for nexttoken in graph[token]:
                    if nexttoken not in visited:
                        visited.add(nexttoken)
                        if dfs(nexttoken):
                            return True

            return False

        for token in sentence2:
            if token in sentence1:
                sentence1.remove(token)
            else:
                visited = set()
                find_similar = dfs(token)
                if not find_similar:
                    return False

        return len(sentence1) == 0