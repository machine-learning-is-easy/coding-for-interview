

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.lis = []
        def bfs(root,target):
            if not root:
                return
            if target-root.val in self.lis:
                return True
            self.lis.append(root.val)
            x = bfs(root.left,target) or bfs(root.right,target)
            return x
        return bfs(root,k)