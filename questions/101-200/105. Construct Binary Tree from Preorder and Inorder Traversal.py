
#questions: does the tree has same value nodes. does the None is in the array?
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # ********

        if len(preorder) == 0:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)

        inorder_index = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:inorder_index + 1], inorder[:inorder_index])
        root.right = self.buildTree(preorder[inorder_index + 1:], inorder[inorder_index + 1:])
        return root