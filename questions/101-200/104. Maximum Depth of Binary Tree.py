
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        stack = []
        if root is not None:
            stack.append(root)

        depth = 0
        while stack:
            for _ in range(len(stack)):
                n = stack.pop(0)
                if n is not None:
                    if n.left:
                        stack.append(n.left)
                    if n.right:
                        stack.append(n.right)
            depth += 1

        return depth


