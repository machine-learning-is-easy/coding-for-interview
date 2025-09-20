
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        total = 0
        if root:
            if root.val < low:
                total += self.rangeSumBST(root.right, low, high)
            elif root.val > high:
                total += self.rangeSumBST(root.left, low, high)
            else:
                total += root.val
                total += self.rangeSumBST(root.left, low, high)
                total += self.rangeSumBST(root.right, low, high)

            return total
        else:
            return 0
