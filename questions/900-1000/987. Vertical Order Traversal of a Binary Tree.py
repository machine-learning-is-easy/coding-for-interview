
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = defaultdict(list)

        def dfs(node, column):
            res[column].append(node.val)
            if node.left:
                dfs(node.left, column - 1)

            if node.right:
                dfs(node.right, column + 1)

        dfs(root, 0)

        min_key = min(list(res.keys()))
        result = []
        while min_key in res:
            result.append(res[min_key])
            min_key += 1
        return result



class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []

        def BFS(root):
            queue = deque([(root, 0, 0)])
            while queue:
                node, row, column = queue.popleft()
                if node is not None:
                    node_list.append((column, row, node.val))
                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        # step 1). construct the global node list, with the coordinates
        BFS(root)

        # step 2). sort the global node list, according to the coordinates
        node_list.sort()

        # step 3). retrieve the sorted results partitioned by the column index
        ret = OrderedDict()
        for column, row, value in node_list:
            if column in ret:
                ret[column].append(value)
            else:
                ret[column] = [value]

        return list(ret.values())