

class WordDictionary:

    def __init__(self):
        self.word = {}

    def addWord(self, word: str) -> None:
        w = self.word
        for c in word:
            if c not in w:
                w[c] = {}
            w = w[c]
        w["$"] = {}

    def search(self, word: str) -> bool:
        cur = self.word
        def dfs(ind, cur):
            if ind == len(word):
                if "$" in cur:
                    return True
                else:
                    return False
            else:
                if word[ind] == ".":
                    for key in cur:
                        if dfs(ind + 1, cur[key]):
                            return True
                    return False
                else:
                    if word[ind] in cur:
                        return dfs(ind + 1, cur[word[ind]])
                    else:
                        return False

        return dfs(0, cur)