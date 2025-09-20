

# need to ask question root to leaf or root to any node

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, target):
            # the end condition may be different for root to any node.
            # if any node the condition will be
            # if node and node.val == target
            if node.left is None and node.right is None and target == node.val:
                return True

            # try left child node
            if node.left:

                if dfs(node.left, target - node.val):
                    return True
            # try right child node
            if node.right:
                if dfs(node.right, target - node.val):
                    return True

            return False

        return dfs(root, targetSum)