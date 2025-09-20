
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sametree(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 is None:
                return False
            elif root2 is None:
                return False
            else:
                if root1.val == root2.val:
                    return sametree(root1.left, root2.left) and sametree(root1.right, root2.right)
                else:
                    return False

        def dfs(node):
            if not node:
                return False
            else:
                if sametree(node, subRoot):
                    return True
                else:
                    return dfs(node.right) or dfs(node.left)

        return dfs(root)

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

            def same_tree(node1, node2):
                if not node1 and not node2:
                    return True
                elif node1 and node2:
                    return node1.val == node2.val and same_tree(node1.left, node2.left) and same_tree(node1.right,
                                                                                                      node2.right)
                else:
                    return False

            if not root and not subRoot:
                return True
            elif root and subRoot:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or same_tree(root,
                                                                                                              subRoot)
            else:
                return False

