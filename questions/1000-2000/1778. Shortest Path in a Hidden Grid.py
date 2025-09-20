
class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        from collections import deque

        DIRS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        REVERSE = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

        grid = {}
        target = [None]  # coordinates of the target
        visited = set()

        def dfs(x, y):
            if (x, y) in visited:
                return
            visited.add((x, y))
            if master.isTarget():
                target[0] = (x, y)
            grid[(x, y)] = True

            for d, (dx, dy) in DIRS.items():
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and master.canMove(d):
                    master.move(d)
                    dfs(nx, ny)
                    master.move(REVERSE[d])  # backtrack

        # Step 1: Explore the map from (0, 0)
        dfs(0, 0)

        if target[0] is None:
            return -1

        # Step 2: BFS to find shortest path to target
        queue = deque()
        queue.append((0, 0, 0))  # (x, y, distance)
        seen = set()
        seen.add((0, 0))

        while queue:
            x, y, dist = queue.popleft()
            if (x, y) == target[0]:
                return dist
            for dx, dy in DIRS.values():
                nx, ny = x + dx, y + dy
                if (nx, ny) in grid and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    queue.append((nx, ny, dist + 1))

        return -1

