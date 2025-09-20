

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.word = ''

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()  # children is self object
            node = node.children[c]
        node.word = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        if node.word != word:
            return False
        else:
            return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for letter in prefix:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
        return True
