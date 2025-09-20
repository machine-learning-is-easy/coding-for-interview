
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.d = dict()
        def dfs(node, i):
            if not(node): return 0
            self.d[i] = node
            return 1 + dfs(node.left, 2*i) + dfs(node.right, 2*i+1)
        self.root = root
        self.l = dfs(root, 1)

    def insert(self, val: int) -> int:
        self.l += 1
        self.d[self.l] = TreeNode(val)
        if(self.l % 2):
            self.d[self.l//2].right = self.d[self.l]
        else:
            self.d[self.l//2].left = self.d[self.l]
        return self.d[self.l//2].val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()