

from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        # convert to list mod 60
        converted = [t % 60 for t in time]
        num = 0
        hash_table = defaultdict(int)
        for ind in range(len(converted)):
            if (60 - converted[ind]) % 60 in hash_table:
                num += hash_table[(60 - converted[ind]) % 60]

            hash_table[converted[ind]] += 1

        return num