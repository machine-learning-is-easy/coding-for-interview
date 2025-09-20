


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        # find all 1s
        rows = len(grid)
        cols = len(grid[0])

        starts = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    starts.append((r, c))

        dis_hash = defaultdict(list)
        surrounding_cell = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for r, c in starts:
            # BFS with (r, c)
            queue = [(r, c)]
            visited = set([(r, c)])
            distance = 0
            while queue:
                for _ in range(len(queue)):
                    cell = queue.pop(0)
                    dis_hash[cell].append(distance)
                    for dr, dc in surrounding_cell:
                        new_r = cell[0] + dr
                        new_c = cell[1] + dc
                        if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited:
                            queue.append((new_r, new_c))
                            visited.add((new_r, new_c))

                distance += 1

        min_distance = float("inf")

        for key, dis_list in dis_hash.items():
            min_distance = min(min_distance, sum(dis_list))

        return min_distance

"""
inverse thinking, find all distance to all 1s for all cells. then sum each cell to all 1s.
"""