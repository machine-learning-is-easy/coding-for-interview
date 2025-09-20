

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        values = set([p.val, q.val])
        def dfs(node):
            if not node:
                return 0, None
            else:
                l, r = dfs(node.left), dfs(node.right)
                if node.val in values:
                    return l[0] + r[0] + 1, node
                else:
                    if l[0] == 2:
                        return l
                    elif r[0] == 2:
                        return r
                    else:
                        return l[0] + r[0], node
        matched, node = dfs(root)
        if matched == 2:
            return node
        else:
            return None