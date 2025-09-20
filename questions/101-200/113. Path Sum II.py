
"""
questions: 
Does the nodes include negative values:
Does the nodes include zero values
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []

        def backtracking(root, target, tmp):
            if root:
                if root.left is None and root.right is None:  # leave
                    if target == root.val:
                        tmp.append(root.val)
                        res.append(list(tmp))
                        tmp.pop(-1)
                else:
                    tmp.append(root.val)
                    if root.left:
                        backtracking(root.left, target - root.val, tmp)
                    if root.right:
                        backtracking(root.right, target - root.val, tmp)
                    tmp.pop(-1)

        backtracking(root, targetSum, [])
        return res