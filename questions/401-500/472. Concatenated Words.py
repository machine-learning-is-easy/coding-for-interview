

# sort the array by the length of the element, adding the element to a set, for the next word, check if it is can be
# get from catenated from previous word.
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        def dfs(word, word_dict):
            if word == "":
                return True
            else:
                for w in word_dict:
                    if word[:len(w)] == w and dfs(word[len(w):], word_dict):
                        return True
                return False

        words.sort(key=lambda x: len(x))
        word_dict = set()
        res = []
        for word in words:
            if dfs(word, word_dict):
                res.append(word)
            else:
                word_dict.add(word)
        return res