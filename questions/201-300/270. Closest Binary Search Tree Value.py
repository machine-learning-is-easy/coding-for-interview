
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        min_distance = abs(root.val - target)
        min_node = [root.val]
        def find_min(node, target):
            nonlocal min_node
            nonlocal min_distance
            if not node:
                return
            else:
                if node.val < target:
                    if abs(node.val - target) < min_distance:
                        min_node = [node.val]
                        min_distance = abs(node.val - target)
                    elif abs(node.val - target) == min_distance:
                        min_node.append(node.val)
                    find_min(node.right, target)

                elif node.val > target:
                    if abs(node.val - target) < min_distance:
                        min_node = [node.val]
                        min_distance = abs(node.val - target)
                    elif abs(node.val - target) == min_distance:
                        min_node.append(node.val)

                    find_min(node.left, target)
                else:
                    if abs(node.val - target) < min_distance:
                        min_node = [node.val]
                        min_distance = abs(node.val - target)
                    elif abs(node.val - target) == min_distance:
                        min_node.append(node.val)
                    return

        find_min(root, target)
        if min_node:
            min_val_sorted = sorted(min_node)
            return min_val_sorted[0]
        else:
            return None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# no need to record a list of min_node, just record the min_val
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        min_d = abs(root.val - target)
        min_val = root.val

        def dfs(node):
            nonlocal min_d
            nonlocal min_val
            if not node:
                return
            else:
                if abs(node.val - target) < min_d or (abs(node.val - target) == min_d and node.val < min_val):
                    mid_d = abs(node.val - target)
                    min_val = node.val

                if node.val < target:
                    dfs(node.right)

                elif node.val > target:
                    dfs(node.left)

                else:
                    return

        return min_val
