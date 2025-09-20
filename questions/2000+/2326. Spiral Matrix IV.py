
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        cur = head
        r, c = 0, 0
        matrix = [[-1] * n for _ in range(m)]
        step = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_d = 0
        visited = set()
        while step < m * n:
            if cur:
                matrix[r][c] = cur.val
            else:
                return matrix
            cur = cur.next
            visited.add((r, c))
            dr, dc = directions[cur_d]
            if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited:
                r = r + dr
                c = c + dc
            else:
                cur_d = (cur_d + 1) % 4
                dr, dc = directions[cur_d]
                r = r + dr
                c = c + dc
            step += 1
        return matrix