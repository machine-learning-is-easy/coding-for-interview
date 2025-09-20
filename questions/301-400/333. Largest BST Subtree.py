

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def postOrder(root):
            if not root:
                # min value is +inf /  max value is -inf
                # Since if null node to left then its max < root.val
                # And if null node to right then its min < root.val
                # As we set min as +inf and max as -inf this will be true
                return (math.inf, -math.inf, 0)

            leftMin, leftMax, leftNodes = postOrder(root.left)
            rightMin, rightMax, rightNodes = postOrder(root.right)
            # For a parent to be BST its left trees max should be less
            # And its right trees min should be greater
            # Post order we visit child first then parent
            # So we first visit smaller BST then larger.
            if leftMax < root.val < rightMin:
                # We want to know max and min value of all nodes
                # rooted at this root.
                maxVal = max(leftMax, rightMax, root.val)
                minVal = min(leftMin, rightMin, root.val)
                return (minVal, maxVal, leftNodes + rightNodes + 1)
            else:
                # As not a BST we want BST check to fail for all nodes above this node.
                # So min is -inf and max is +inf
                # If left - parent will check max < root.val and fail
                # If right - parent will check root.val < min and fail
                # Bubble up the maxNode from left and right as they can have ans
                return (-math.inf, math.inf, max(leftNodes, rightNodes))

        minVal, maxVal, nodes = postOrder(root)
        return nodes


    def largestBSTSubtree(root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return (float('inf'), float('-inf'), 0, True)  # (min, max, size, isBST)

            left_min, left_max, left_size, left_isBST = helper(node.left)
            right_min, right_max, right_size, right_isBST = helper(node.right)

            if left_isBST and right_isBST and left_max < node.val < right_min:
                size = left_size + right_size + 1
                return (min(left_min, node.val), max(right_max, node.val), size, True)

            return (0, 0, max(left_size, right_size), False)

        return helper(root)[2]
