

class Solution:
    def shortestBridge(self, grid) -> int:
        def dfs(x, y):
            grid[x][y] = 2
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 1:
                        dfs(nx, ny)
                    elif grid[nx][ny] == 0: # add the first seen 0 in to a list.
                        q.add((nx, ny))

        m, n = len(grid), len(grid[0])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = set()

        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                dfs(i, j)  # paint one island to 2, border 0 add to q
                break

        # breath first search the first seen 0s
        step = 0
        q = deque(q)
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1: return step + 1
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2  # mark visited
                            q.append((nx, ny))
            step += 1

        return step

assert Solution().shortestBridge([[1,1,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]) == 3

# a minor change to the above code.
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start_i, start_j = next((i, j) for i in range(m) for j in range(n) if grid[i][j])

        stack = [(start_i, start_j)]
        visited = set(stack)
        while stack:
            i, j = stack.pop()
            visited.add((i, j))
            for ii, jj in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] and (ii, jj) not in visited:
                    stack.append((ii, jj))
                    visited.add((ii, jj))

        ans = 0
        queue = list(visited)
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                for ii, jj in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in visited:
                        if grid[ii][jj] == 1:
                            return ans
                        queue.append((ii, jj))
                        visited.add((ii, jj))
            ans += 1