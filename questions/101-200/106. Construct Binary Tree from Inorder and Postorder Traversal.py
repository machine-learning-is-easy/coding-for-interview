

# need to ask if the vals are different or the same
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        else:
            val = postorder[-1]
            node = TreeNode(val=val)

            left_inorder = inorder[:inorder.index(val)]
            left_postorder = postorder[:len(left_inorder)]

            right_inorder = inorder[inorder.index(val) + 1:]
            right_postorder = postorder[:-1][-len(right_inorder):]

            node.left = self.buildTree(left_inorder, left_postorder)
            node.right = self.buildTree(right_inorder, right_postorder)

            return node