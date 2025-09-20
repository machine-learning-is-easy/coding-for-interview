
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_path = 0

        def dfs(node):
            nonlocal max_path
            if not node:
                return 0
            else:
                l, r = dfs(node.left), dfs(node.right)

                if node.left:
                    if node.val == node.left.val - 1:
                        left_path = l + 1
                    else:
                        left_path = 1
                else:
                    left_path = 1

                if node.right:
                    if node.val == node.right.val - 1:
                        right_path = r + 1
                    else:
                        right_path = 1
                else:
                    right_path = 1

                max_path = max(max_path, max(right_path, left_path))
                return max(right_path, left_path)

        dfs(root)
        return max_path