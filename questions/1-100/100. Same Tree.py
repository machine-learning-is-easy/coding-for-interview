
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p == None and q == None:
            return True
        elif p != None and q != None:
            if p.val == q.val:
                return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
            else:
                return False
        else:
            return False