

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        full_sug = []
        for ind in range(len(searchWord)):
            suggest_list = [item for item in products if item.startswith(searchWord[:ind+1])]
            suggest_list.sort(reverse=False)
            full_sug.append(suggest_list[:3])
        return full_sug

# another version is building trie


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None  # Set at leaf node


class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()  # Ensure lexicographic order

        # Step 1: Build Trie
        root = TrieNode()
        for product in products:
            node = root
            for char in product:
                node = node.children[char]
            node.word = product  # Mark word at the leaf

        # Step 2: DFS from current node to collect up to 3 words
        def dfs(node, path, res):
            if len(res) == 3:
                return
            if node.word:
                res.append(node.word)
            for char in sorted(node.children.keys()):
                dfs(node.children[char], path + char, res)

        # Step 3: Traverse Trie by searchWord and collect suggestions
        result = []
        node = root
        for char in searchWord:
            if node:
                node = node.children.get(char)
            if node:
                suggestions = []
                dfs(node, "", suggestions)
                result.append(suggestions)
            else:
                result.append([])

        return result