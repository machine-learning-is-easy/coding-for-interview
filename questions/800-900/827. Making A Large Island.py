

class Solution:
    def largestIsland(self, grid) -> int:
        class UF:
            def __init__(self):
                self.sets = {}
                self.size = {}

            def find(self, i, j):
                if self.sets[(i, j)] == (i, j):
                    return (i, j)
                val = (i, j)
                p_i, p_j = self.sets[val]
                parent = self.find(p_i, p_j)
                self.sets[(i, j)] = parent
                return parent

            def make_set(self, i, j):
                self.sets[(i, j)] = (i, j)

            def union(self, i1, j1, i2, j2):
                p1 = self.find(i1, j1)
                self.make_set(i2, j2)
                self.sets[(i2, j2)] = p1

            def update_size(self, i, j, size):
                i_p, j_p = self.find(i, j)
                self.size[(i_p, j_p)] = size

            def get_size(self, i, j):
                parent = self.find(i, j)
                return self.size[parent]

        n = len(grid)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vis = [[False for _ in range(n)] for _ in range(n)]
        uf = UF()

        def in_bounds(i, j):
            if 0 <= i < n and 0 <= j < n:
                return True
            return False

        def bfs(i, j):
            q = deque([(i, j)])
            comp_size = 0
            uf.make_set(i, j)
            vis[i][j] = True

            while len(q):
                c_i, c_j = q.popleft()
                uf.union(i, j, c_i, c_j)
                comp_size += 1
                for d_i, d_j in dirs:
                    new_i, new_j = c_i + d_i, c_j + d_j
                    if in_bounds(new_i, new_j) and not vis[new_i][new_j] and grid[new_i][new_j] == 1:
                        vis[new_i][new_j] = True
                        q.append((new_i, new_j))
            uf.update_size(i, j, comp_size)
            return comp_size

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not vis[i][j]:
                    # perform bfs, get the size of the component, asign the size to that set
                    # make all the components elements point to the element
                    comp_size = bfs(i, j)
                    if comp_size == n * n:
                        return n * n

        def handle_zero(i, j):
            max_union = 1
            seen_components = set()

            for d_i, d_j in dirs:
                new_i, new_j = i + d_i, j + d_j

                if in_bounds(new_i, new_j) and grid[new_i][new_j] == 1:
                    parent = uf.find(new_i, new_j)
                    if parent not in seen_components:
                        seen_components.add(parent)
                        max_union += uf.get_size(new_i, new_j)

            return max_union

        max_island = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    max_island = max(max_island, handle_zero(i, j))
        return max_island

# grid = [[1,0],[0,1]]
#
# assert Solution().largestIsland(grid) == 3

# timeout version
class Solution:
    def largestIsland(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        max_island = 0

        def bfs_cell(r, c):
            visited = set()
            visited.add((r, c))
            queue = [(r, c)]
            count = 1
            while queue:
                r, c = queue.pop(0)
                suround = ((0, 1), (1, 0), (0, -1), (-1, 0))
                for dx, dy in suround:
                    new_r, new_c = r + dx, c + dy
                    if 0 <= new_r < row and 0 <= new_c < col and (new_r, new_c) not in visited and grid[new_r][new_c] == 1:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
                        count += 1
            return count


        for r in range(row):
            for c in range(col):
                max_island = max(max_island, bfs_cell(r, c))
        return max_island

# start every 0 cell, check the size of the island.
class Solution(object):
    def largestIsland(self, grid):
        N = len(grid)

        def check(r, c):
            seen = {(r, c)}
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                    if (nr, nc) not in seen and 0 << N and 0 <= nc < N and grid[nr][nc]:
                        stack.append((nr, nc))
                        seen.add((nr, nc))
            return len(seen)

        ans = 0
        has_zero = False
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 0:
                    has_zero = True
                    grid[r][c] = 1
                    ans = max(ans, check(r, c))
                    grid[r][c] = 0

        return ans if has_zero else N*N


class Solution:
    def largestIsland(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        max_island = 0
        cell_value = {}
        origin_cell = {}
        def bfs_cell(r, c):
            nonlocal origin_cell, cell_value
            visited = set()
            visited.add((r, c))
            queue = [(r, c)]
            origin_cell[(r, c)] = (r, c)
            count = 1
            while queue:
                r, c = queue.pop(0)
                suround = ((0, 1), (1, 0), (0, -1), (-1, 0))
                for dx, dy in suround:
                    new_r, new_c = r + dx, c + dy
                    if (new_r, new_c) in origin_cell and origin_cell[(new_r, new_c)] in cell_value:
                        count += cell_value[origin_cell[(new_r, new_c)]]
                    elif 0 <= new_r < row and 0 <= new_c < col and (new_r, new_c) not in visited and grid[new_r][new_c] == 1:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
                        origin_cell[(new_r, new_c)] = (r, c)
                        count += 1
            if grid[r][c] == 1:
                cell_value[(r, c)] = count
            return count

        has_zero = False
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    has_zero = True
                    value = bfs_cell(r, c)
                    max_island = max(max_island, value)
        return max_island if has_zero else col * row


class Solution:
    def largestIsland(self, grid) -> int:
        class UF:
            def __init__(self):
                self.sets = {}
                self.size = {}

            def set_parent(self, i, j, parent):
                self.sets[(i, j)] = parent

            def get_parent(self, i, j):
                if (i, j) in self.sets:
                    i_p, j_p = self.sets[(i, j)]
                    if (i_p, j_p) == (i, j):
                        return (i, j)
                    parent = self.get_parent(i_p, j_p)
                    self.sets[(i, j)] = parent
                    return parent
                else:
                    return None

            def union(self, i1, j1, i2, j2):
                parent = self.get_parent(i1, j1)
                self.set_parent(i2, j2, parent)

            def set_size(self, i, j, size):
                self.size[(i, j)] = size

            def get_size(self, parent):
                return self.size[parent]

        visited = set()
        row = len(grid)
        col = len(grid[0])
        uf = UF()

        def BFS(i, j):
            area = 1
            nonlocal visited
            queue = [(i, j)]
            uf.set_parent(i, j, (i, j))
            while queue:
                r, c = queue.pop(0)
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_r, new_c = r + dx, c + dy
                    if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == 1 and (
                    new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
                        area += 1
                        uf.union(i, j, new_r, new_c)
            uf.set_size(i, j, area)

        # create union found
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c))
                    BFS(r, c)
        print(uf.sets)

        def search_zero(i, j):
            visited_parent = set()
            area = 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r, new_c = i + dx, j + dy
                if (new_r, new_c) in uf.sets and grid[new_r][new_c] == 1:
                    parent = uf.get_parent(new_r, new_c)
                    if parent not in visited_parent:
                        area += uf.get_size(parent)
                        visited_parent.add(parent)
            return area

        visited = set()
        max_island = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    num = search_zero(r, c)
                    max_island = max(max_island, num)

        return max_island

grid = [[1,1],[1,1]]

assert Solution().largestIsland(grid) == 1


# another version is mark the island with index
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # step 1: mark index in grid
        def dfs(r, c, index):
            grid[r][c] = index
            size = 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    size += dfs(nr, nc, index)

            return size

        index = 2
        island_size = {0: 0}

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:  # != 0 is not right, since we marked celss
                    island_size[index] = dfs(r, c, index)
                    index += 1

        # step 2: try connection
        max_size = max(island_size.values())
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    size = 1  # adding the current change
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = dr + r, dc + c
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])  # remove duplicate

                    for index in seen:
                        size += island_size[index]

                    max_size = max(max_size, size)

        return max_size


# works solution below
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        row_n = len(grid)
        col_n = len(grid[0])
        max_area = 0

        def dfs(r, c, v, visited):
            grid[r][c] = v
            visited.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < row_n and 0 <= new_c < col_n and grid[new_r][new_c] == 1:
                    dfs(new_r, new_c, v, visited)

        tag = 2
        tag_n = {0: 0}
        for r in range(row_n):
            for c in range(col_n):
                if grid[r][c] == 1:
                    visited = set()
                    dfs(r, c, tag, visited)
                    tag_n[tag] = len(visited)
                    tag += 1
        print(tag_n)
        for r in range(row_n):
            for c in range(col_n):
                seen = set()
                if grid[r][c] == 0:
                    total_area = 1
                else:
                    total_area = 0
                    seen.add(grid[r][c])
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < row_n and 0 <= new_c < col_n and grid[new_r][new_c] != 0:
                        seen.add(grid[new_r][new_c])

                for v in seen:
                    total_area += tag_n[v]
                max_area = max(max_area, total_area)
        return max_area