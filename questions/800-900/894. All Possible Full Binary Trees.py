
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1:
            return [TreeNode()]

        result = []
        for k in range(1, n - 1, 2):
            for left in self.allPossibleFBT(k):
                for right in self.allPossibleFBT(n - 1 - k):
                    result.append(TreeNode(0, left, right))

        return result