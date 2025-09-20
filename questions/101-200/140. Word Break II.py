

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        from copy import deepcopy
        wordSet = set(wordDict)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        memo = []

        # @lru_cache(maxsize=None)    # alternative memoization solution
        def _wordBreak_topdown(s, word_list):
            """ return list of word lists """
            if not s:
                memo.append(deepcopy(word_list))
                return

            for w in wordSet:
                if s[:len(w)] == w:
                    word_list.append(w)
                    _wordBreak_topdown(s[len(w):], word_list)
                    word_list.pop(-1)

        # break the input string into lists of words list

        _wordBreak_topdown(s, [])

        # chain up the lists of words into sentences.
        return [" ".join(words) for words in memo]

# assert Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"]) == ["cats and dog","cat sand dog"]
assert Solution().wordBreak("aaaaaaa", ["a", "aa","aaaa"]) == ["a a a a a a a","aa a a a a a","a aa a a a a","a a aa a a a","aa aa a a a","aaaa a a a","a a a aa a a","aa a aa a a","a aa aa a a","a aaaa a a","a a a a aa a","aa a a aa a","a aa a aa a","a a aa aa a","aa aa aa a","aaaa aa a","a a aaaa a","aa aaaa a","a a a a a aa","aa a a a aa","a aa a a aa","a a aa a aa","aa aa a aa","aaaa a aa","a a a aa aa","aa a aa aa","a aa aa aa","a aaaa aa","a a a aaaa","aa a aaaa","a aa aaaa"]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)  # Use a set for O(1) lookup
        memo = {}  # Memoization dictionary

        def backtracking(substr):
            if substr in memo:
                return memo[substr]
            if not substr:
                return [""]  # Base case: return empty string to join words correctly

            res = []
            for word in wordSet:
                if substr.startswith(word):
                    suffix_ways = backtracking(substr[len(word):])
                    for suffix in suffix_ways:
                        res.append(word + (" " + suffix if suffix else ""))  # Handle spacing correctly

            memo[substr] = res  # Store the computed result
            return res

        return backtracking(s)

# assert Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"]) == ["cats and dog","cat sand dog"]
assert Solution().wordBreak("aaaaaaa", ["a", "aa","aaaa"]) == ["a a a a a a a","aa a a a a a","a aa a a a a","a a aa a a a","aa aa a a a","aaaa a a a","a a a aa a a","aa a aa a a","a aa aa a a","a aaaa a a","a a a a aa a","aa a a aa a","a aa a aa a","a a aa aa a","aa aa aa a","aaaa aa a","a a aaaa a","aa aaaa a","a a a a a aa","aa a a a aa","a aa a a aa","a a aa a aa","aa aa a aa","aaaa a aa","a a a aa aa","aa a aa aa","a aa aa aa","a aaaa aa","a a a aaaa","aa a aaaa","a aa aaaa"]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(index: int) -> List[str]:
            if index in memo:
                return memo[index]
            if index == len(s):
                return [""]

            sentences = []
            for end in range(index + 1, len(s) + 1):
                word = s[index:end]
                if word in word_set:
                    for sentence in backtrack(end):
                        sentences.append(word + (" " + sentence if sentence else ""))

            memo[index] = sentences
            return sentences


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)

        @cache
        def backtracking(substring):
            if not substring:
                return [""]
            combo = []
            for i, _ in enumerate(substring):
                w = substring[:i + 1]
                if w in wordset:
                    combo.extend([f'{w} {sentence}' if sentence else w
                                  for sentence in backtracking(substring[i + 1:])])
            return combo

        return backtracking(s)
# time complexity is

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)

        @cache
        def dfs(ind):
            if ind == len(s):
                return [""]
            res = []
            for i in range(ind, len(s)):
                cur_word = s[ind:i+1]
                if cur_word in wordset:
                    candidates = dfs(i+1)
                    print(candidates)
                    for c in candidates:
                        if c:
                            res.append(cur_word + " " + c)
                        else:
                            res.append(cur_word)
            return res

        return dfs(0)
# time complexity is