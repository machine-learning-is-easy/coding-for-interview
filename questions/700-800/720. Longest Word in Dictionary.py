

class Solution:
    def longestWord(self, words: List[str]) -> str:
        hash_set = set()

        result = ''
        words = sorted(words)

        for w in words:
            if len(w) == 1 or w[:-1] in hash_set:
                if len(w) > len(result):
                    result = w
                hash_set.add(w)

        return result

