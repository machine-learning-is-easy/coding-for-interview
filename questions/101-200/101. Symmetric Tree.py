
class Solution:

    # *****
    def isSymmetric(self, root: TreeNode) -> bool:

        def symmetric(nod1, nod2):
            if nod1 is None and nod2 is None:
                return True
            elif nod1 is None or nod2 is None:
                return False
            else:
                return nod1.val == nod2.val and symmetric(nod1.right, nod2.left) and symmetric(nod1.left, nod2.right)

        return symmetric(root, root)