

class TrieNode:
    def __init__(self):
        self.children = {}
        self.indices = set()

class WordFilter:
    def __init__(self, words):
        self.prefix_root = TrieNode()
        self.suffix_root = TrieNode()

        for index, word in enumerate(words):
            # Insert into prefix trie
            node = self.prefix_root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.indices.add(index)

            # Insert into suffix trie (reversed word)
            node = self.suffix_root
            for char in reversed(word):
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.indices.add(index)

        self.words = words

    def f(self, pref, suff):
        # Traverse prefix trie
        node = self.prefix_root
        for char in pref:
            if char not in node.children:
                return -1
            node = node.children[char]
        prefix_indices = node.indices

        # Traverse suffix trie
        node = self.suffix_root
        for char in reversed(suff):
            if char not in node.children:
                return -1
            node = node.children[char]
        suffix_indices = node.indices

        # Find max common index
        common = prefix_indices & suffix_indices
        return max(common) if common else -1