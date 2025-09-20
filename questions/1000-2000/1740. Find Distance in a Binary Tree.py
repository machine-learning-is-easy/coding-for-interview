
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0

        def dfs(node):
            """Traverse the tree post-order."""
            # fn has two returns, (number_of_node_found, distance_to_the_node)
            if not node: return 0, 0
            ltf, lv = dfs(node.left)
            rtf, rv = dfs(node.right)

            # relay the result of left and right branch
            if node.val in (p, q):
                if ltf or rtf:
                    return max(ltf, rtf) + 1, max(lv, rv) + 1  # return left or right found nodes and level
                else:
                    return 1, 0
            else:
                if ltf == 2:
                    return ltf, lv
                if rtf == 2:
                    return rtf, rv

                if ltf == 1 and rtf == 1:
                    return rtf + ltf, lv + rv + 2
                elif ltf:
                    return ltf, lv + 1
                elif rtf:
                    return rtf, rv + 1
                else:
                    return 0, 0

        n_node_found, depth = dfs(root)
        return depth
