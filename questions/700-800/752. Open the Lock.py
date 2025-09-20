
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i + 1:]

        queue = ["0000"]

        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        visited = set("0000")
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                cur = queue.pop(0)
                for nei in neighbors(cur):
                    if nei in deadends or nei in visited:
                        continue
                    elif nei == target:
                        return step
                    else:
                        visited.add(nei)
                        queue.append(nei)

        return -1