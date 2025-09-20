
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # **********
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0

            # max sum on the left and right sub-trees of node
            # the maximum does not necessary include current node.
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain

            # update max_sum if it's better to start a new path
            max_sum = max(max_sum, price_newpath)

            # for recursion :
            # return the max gain if continue the same path, need includes current node, not necessary to include
            # left or right child
            return node.val + max(left_gain, right_gain, 0)

        max_sum = float('-inf')
        max_gain(root)
        return max_sum