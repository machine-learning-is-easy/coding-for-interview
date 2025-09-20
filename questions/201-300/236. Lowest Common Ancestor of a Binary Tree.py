

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        p_path = None
        q_path = None

        p_path_stack = []
        q_path_stack = []

        def findpth(node):
            # find a path of node
            nonlocal p_path, q_path, p_path_stack, q_path_stack
            if node is None:
                return

            if p_path is not None and q_path is not None:
                return

            p_path_stack.append(node)
            q_path_stack.append(node)

            if node.val == p.val:
                p_path = list(p_path_stack)

            if node.val == q.val:
                q_path = list(q_path_stack)

            findpth(node.left)
            findpth(node.right)

            p_path_stack.pop(-1)
            q_path_stack.pop(-1)

        findpth(root)

        indx = 0
        while indx < min(len(p_path), len(q_path)):
            if p_path[indx].val != q_path[indx].val:
                break

            indx += 1
        return p_path[indx - 1].val


# more concise version
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        val_set = set([p.val, q.val])

        def dfs(node):
            if not node:
                return 0, None

            l, r = dfs(node.left), dfs(node.right)

            if node.val in val_set:
                return l[0] + r[0] + 1, node
            else:
                if l[0] == 2:
                    return l
                elif r[0] == 2:
                    return r
                else:
                    return l[0] + r[0], node
        return dfs(root)[1]

# simple solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        val_set = set([p.val, q.val])

        def lca(node):
            if not node or node.val in val_set:
                return node
            else:
                left = lca(node.left)
                right = lca(node.right)
                return node if left and right else left or right

        return lca(root)