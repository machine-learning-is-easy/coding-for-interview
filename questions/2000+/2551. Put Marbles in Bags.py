
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1:
            return 0  # All marbles go into one bag, only one possible distribution

        # Calculate the cost between adjacent marbles, i.e., weights[i] + weights[i+1]
        pair_costs = [weights[i] + weights[i+1] for i in range(n - 1)]

        # To maximize the score: pick (k-1) largest cuts
        max_score = sum(sorted(pair_costs, reverse=True)[:k-1])

        # To minimize the score: pick (k-1) smallest cuts
        min_score = sum(sorted(pair_costs)[:k-1])

        return max_score - min_score