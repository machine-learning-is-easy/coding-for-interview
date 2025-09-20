
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = defaultdict(int)
        back = 0
        max_len = 0
        for front, char in enumerate(answerKey):
            count[char] += 1
            if front - back + 1 - max(count.values()) > k:
                count[answerKey[back]] -= 1
                back += 1
            else:
                max_len = max(max_len, front - back + 1)

        return max_len