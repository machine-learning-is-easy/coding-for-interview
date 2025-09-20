

from collections import defaultdict


class TrieNode:

    def __init__(self, name):
        self.name = name
        self.is_file = False
        self.content = ""
        self.next = defaultdict(TrieNode)


class FileSystem:

    def __init__(self):
        self.head = TrieNode("")

    def ls(self, path: str) -> List[str]:
        cur = self.findPath(path)

        if cur.is_file:
            return [cur.name]

        res = [p for p in cur.next]
        res.sort()
        return res

    def mkdir(self, path: str) -> None:
        self.findPath(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.findPath(filePath)
        cur.is_file = True
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.findPath(filePath)
        return cur.content

    def findPath(self, filepath: str) -> TrieNode:
        cur = self.head
        if filepath == "/":
            return cur

        paths = filepath.split("/")[1:]

        for p in paths:
            if p not in cur.next:
                cur.next[p] = TrieNode(p)
            cur = cur.next[p]

        return cur
