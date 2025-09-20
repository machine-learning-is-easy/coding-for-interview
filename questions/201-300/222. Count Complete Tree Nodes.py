
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        num_nodes = 0
        if root == None:
            return 0
        else:
            num_nodes += 1
            num_nodes += self.countNodes(root.left)
            num_nodes += self.countNodes(root.right)
            return num_nodes
