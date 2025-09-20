

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return

        m, n = len(rooms), len(rooms[0])
        INF = 2147483647
        queue = deque()

        # Step 1: Add all gates to the queue
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: BFS from all gates
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Skip if out of bounds or not an empty room
                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == INF:
                    rooms[nx][ny] = rooms[x][y] + 1
                    queue.append((nx, ny))