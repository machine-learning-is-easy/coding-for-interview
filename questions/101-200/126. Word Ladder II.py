

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        def find_distance_w(w):
            return_list = []
            for word in wordList:
                distance = 0
                for w1, w2 in zip(w, word):
                    if w1 != w2:
                        distance += 1
                if distance == 1:
                    return_list.append(word)
            return return_list

        queue = [[beginWord]]
        results = []
        while queue:
            for ind in range(len(queue)):
                word_sq = queue.pop(0)
                # find the distance of 1 with word from dictionary
                one_distance = find_distance_w(word_sq[-1])
                if endWord in one_distance:
                    results.append(word_sq + [endWord])
                else:
                    sub_sq = []
                    for w in one_distance:
                        if w not in word_sq:
                            sub_sq.append(word_sq + [w])
                    queue += sub_sq

            if results:
                return results


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        graph = defaultdict(list)
        for word in wordList:
            for n in range(len(word)):
                key = word[:n] + '*' + word[n + 1:]
                graph[key].append(word)

        queue = [(beginWord, [beginWord])]
        visited = set([beginWord])
        res = []
        while queue:
            for _ in range(len(queue)):
                bgword, path = queue.pop(0)
                for idx in range(len(bgword)):
                    key = bgword[:idx] + "*" + bgword[idx + 1:]
                    if key in graph:
                        for nxt_word in graph[key]:
                            if nxt_word == endWord:
                                res.append(path + [nxt_word])
                            else:
                                if nxt_word not in path:
                                    queue.append((nxt_word, path + [nxt_word]))
                                    visited.add(nxt_word)

            if res != []:
                return res
        return res

