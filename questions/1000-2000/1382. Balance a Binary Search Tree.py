
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)

        dfs(root)

        def balance(left = 0, right = len(nums) - 1):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = balance(left, mid - 1)
            node.right = balance(mid + 1, right)

            return node

        return balance()