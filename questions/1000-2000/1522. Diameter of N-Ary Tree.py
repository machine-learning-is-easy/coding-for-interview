

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            else:
                max_depth = 0
                for child in node.children:
                    depth = dfs(child)
                    diameter = max(diameter, max_depth + depth)
                    max_depth = max(max_depth, depth)
                return max_depth + 1

        dfs(root)
        return diameter