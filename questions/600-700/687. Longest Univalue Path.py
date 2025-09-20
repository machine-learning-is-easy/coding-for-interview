

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        max_len = 0

        def recursive(prev, root):
            nonlocal max_len
            if not root:
                return 0
            left = recursive(root, root.left)
            right = recursive(root, root.right)
            max_len = max(max_len, right + left)

            # return the previous call.
            if prev and root.val == prev.val:
                return 1 + max(left, right)
            return 0

        recursive(None, root)
        return max_len