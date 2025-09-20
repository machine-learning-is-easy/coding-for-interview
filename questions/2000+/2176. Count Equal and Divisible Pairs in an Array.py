

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        value_indices = defaultdict(list)

        # Step 1: Group indices by value
        for idx, val in enumerate(nums):
            value_indices[val].append(idx)

        count = 0

        # Step 2: For each group, check valid pairs
        for indices in value_indices.values():
            n = len(indices)
            for i in range(n):
                for j in range(i + 1, n):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1

        return count