
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            max_tmp = float("-inf")
            for _ in range(len(queue)):
                node = queue.pop(0)
                max_tmp = max(max_tmp, node.val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(max_tmp)
        return res