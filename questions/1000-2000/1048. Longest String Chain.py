

class Solution:
    def longestStrChain(self, words) -> int:
        n = len(words)
        words.sort(key=lambda x: len(x))  # Sort the words according to their length

        dit = {w: 1 for w in words}  # Store the longest word chain length till key word

        for i in range(1, n):
            w = words[i]
            for j in range(len(w)):  # Max len(w) will be 16
                new_w = w[:j] + w[j + 1:]  # new word after removing j-th  character

                # if new_w in dit and dit[new_w] + 1 > dit[w]:
                #     dit[w] = dit[new_w] + 1

                if new_w in dit and dit[new_w] < dit[w] + 1:
                    dit[new_w] = dit[w] + 1

        return max(dit.values())


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=lambda x: len(x), reverse=True)  # Sort the words according to their length

        dit = {w: 1 for w in words}  # Store the longest word chain length till key word
        for i in range(0, n):
            w = words[i]
            for j in range(len(w)):  # Max len(w) will be 16
                new_w = w[:j] + w[j + 1:]  # new word after removing j-th  character

                if new_w in dit and dit[new_w] < dit[w] + 1:
                    dit[new_w] = dit[w] + 1
                    print(dit)

        return max(dit.values())

assert Solution().longestStrChain(["a","b","ba","bca","bda","bdca"]) == 4