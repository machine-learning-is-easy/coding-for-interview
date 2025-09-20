

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0

        for k, freq in count.items():
            group_size = k + 1
            num_groups = math.ceil(freq / group_size)
            total += num_groups * group_size

        return total