

# hint: put value in a dict and put it in order
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        count, row = 0, 0
        hashTable = defaultdict(list)

        def check(node, c, r):

            if node:
                hashTable[(c)].append((node.val, r))
                check(node.left, c - 1, r + 1)
                check(node.right, c + 1, r + 1)

        check(root, count, row)
        result = []

        for k in sorted(hashTable.keys()):
            result.append([v[0] for v in sorted(hashTable[k], key=lambda x: x[1])])

        return result

# BFS version.
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        mp = collections.defaultdict(list)
        min_col = 0
        queue = [(root, 0)]
        res = []
        while queue:
            for _ in range(len(queue)):
                node, col = queue.pop(0)
                min_col = min(min_col, col)
                if col in mp:
                    mp[col].append(node.val)
                else:
                    mp[col] = [node.val]
                if node.left:
                    queue.append((node.left, col - 1))
                if node.right:
                    queue.append((node.right, col + 1))

        while min_col in mp:
            res.append(mp[min_col])
            min_col += 1
        return res

