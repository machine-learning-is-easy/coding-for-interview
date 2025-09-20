
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return 0, None
            l, r = dfs(node.left), dfs(node.right)
            # assume find find the deepest common node
            if l[0] > r[0]:  # left child depth greater than right child, pass the left result
                return l[0] + 1, l[1]
            if l[0] < r[0]: # right child depth greater than left child, pass right child result
                return r[0] + 1, r[1]
            return l[0] + 1, node # left child depth == right child, current node is the
        return dfs(root)[1]