
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def recurse(node):
            if not node:
                return None
            if not(node.left or node.right):
                res[-1].append(node.val)
                return None
            node.left = recurse(node.left)
            node.right = recurse(node.right)
            return node
        while root:
            res.append([])
            root = recurse(root)
        return res