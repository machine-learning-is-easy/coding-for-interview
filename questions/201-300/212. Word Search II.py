

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ### ****************
        WORD_KEY = '$'

        rows, cols = len(board), len(board[0])
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node['$'] = True

        result = []

        def backtrack(i: int, j: int, node=trie, prefix: str = ''):
            letter = board[i][j]
            if letter in node:
                board[i][j] = '#'
                node = node[letter]
                if '$' in node:
                    result.append(prefix + letter)
                    del node['$']  # this word has been found
                for r, c in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= r < rows and 0 <= c < cols:
                        backtrack(r, c, node, prefix + letter)
                board[i][j] = letter

        for i in range(rows):
            for j in range(cols):
                backtrack(i, j)

        return result