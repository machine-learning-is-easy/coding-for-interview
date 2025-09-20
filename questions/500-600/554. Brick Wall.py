

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import Counter

        counter = Counter()

        for row in wall:
            position = 0
            # Don't include the last brick's edge
            for width in row[:-1]:
                position += width
                counter[position] += 1

        if not counter:
            return len(wall)

        # Minimum bricks crossed = total rows - maximum aligned edges
        return len(wall) - max(counter.values())