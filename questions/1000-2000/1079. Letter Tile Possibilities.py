

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            nonlocal count
            for ch in counter:
                if counter[ch] > 0:
                    count += 1  # Count this new sequence
                    counter[ch] -= 1  # Use one occurrence of ch
                    backtrack(counter)  # Recur to build more sequences
                    counter[ch] += 1  # Backtrack and restore the count

        count = 0
        counter = Counter(tiles)  # Count occurrences of each character
        backtrack(counter)
        return count