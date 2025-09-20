
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        max_count = 0
        cur_count = 0
        nodes_num = []

        current_val = None

        def inorder_travers(node):
            nonlocal current_val, max_count, cur_count, nodes_num
            if node is None:
                return
            else:
                inorder_travers(node.left)
                # current node processing
                if node.val == current_val:
                    cur_count += 1
                else:
                    cur_count = 1
                    current_val = node.val

                if cur_count > max_count:
                    nodes_num = [] # reset the
                    nodes_num.append(node.val)
                    max_count = cur_count
                elif cur_count == max_count:
                    nodes_num.append(node.val)

                inorder_travers(node.right)

        inorder_travers(root)

        return nodes_num
