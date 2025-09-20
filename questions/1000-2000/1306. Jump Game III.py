

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        def dfs(ind):
            nonlocal visited
            if arr[ind] == 0:
                return True
            else:
                visited.add(ind)
                for nxt_ind in (ind - arr[ind], ind + arr[ind]):
                    if 0 <= nxt_ind < len(arr) and nxt_ind not in visited:
                        if dfs(nxt_ind):
                            return True
                visited.remove(ind)
            return False

        return dfs(start)