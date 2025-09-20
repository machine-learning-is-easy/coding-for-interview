
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue[0] is not None:
            node = queue.pop(0)
            queue.append(node.left)
            queue.append(node.right)
        return all([n is None for n in queue])