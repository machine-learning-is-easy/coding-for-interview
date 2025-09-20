

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:

        c = 0
        for i in range(1, len(sequence) // len(word) + 1):
            if word * i in sequence:
                c += 1
                continue
            break
        return c

# this solution is not right. when checking previous
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:

        end = 0
        searching_len = len(word)
        start_count = 0

        max_len = 0
        while end <= len(sequence):
            if end < searching_len:
                end += 1
            else:
                if sequence[end - searching_len: end] == word:
                    start_count += 1
                    end += searching_len # this logic is not right.

                else:
                    start_count = 0
                    end += 1

                max_len = max(max_len, start_count)

        return max_len

assert Solution().maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba") == 5

