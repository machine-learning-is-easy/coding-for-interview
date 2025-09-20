

class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        # depth first search
        visited = set()

        def dfs(room_num):
            if room_num in visited:
                return
            else:
                visited.add(room_num)
                for key in rooms[room_num]:
                    dfs(key)

        dfs(0)

        if len(visited) == len(rooms):
            return True
        else:
            return False


assert Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) == False