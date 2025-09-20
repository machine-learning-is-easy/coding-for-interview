

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        node_len = len(nodes)

        node_val = set([node.val for node in nodes])

        def dfs(node):
            if not node:
                return 0, node
            l, r = dfs(node.left), dfs(node.right)

            if node.val in node_val:
                return l[0] + r[0] + 1, node
            else:
                if l[0] == node_len:
                    return l
                if r[0] == node_len:
                    return r
                return l[0] + r[0], node
        
        return dfs(root)[1]