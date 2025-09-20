

class TrieNode:

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = ""


class MagicDictionary:

    def __init__(self):
        self.trie = TrieNode()
        self.s = set()

    def buildDict(self, dictionary: List[str]) -> None:

        for word in dictionary:
            self.s.add(word)
            cur = self.trie
            for ch in word:
                cur = cur.children[ch]
            cur.word = word

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)

        def dfs(root: TrieNode, cnt: int, i: int) -> bool:
            if cnt > 1:
                return False
            if i == n: return cnt == 1 and root.word
            return any([dfs(root.children[c], cnt + int(c != searchWord[i]), i + 1) for c in root.children])

        return dfs(self.trie, 0, 0)

