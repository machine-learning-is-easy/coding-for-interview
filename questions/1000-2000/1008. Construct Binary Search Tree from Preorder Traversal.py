


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def construct(lower, higher, l):
            if not l:
                return None
            elif l[0] < lower or l[0] > higher:
                return None
            else:
                node = TreeNode(val=l.pop(0))
                node.left = construct(lower, node.val, l)
                node.right = construct(node.val, higher, l)

                return node

        root = construct(float("-inf"), float("inf"), preorder)
        return root