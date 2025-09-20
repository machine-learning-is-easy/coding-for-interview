
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # BSF

        node_list = [root]
        ans = 1
        while node_list:
            # get the nodes in the next level

            for _ in range(len(node_list)):
                nod = node_list.pop(0)
                if nod:
                    node_list.append(nod.left)
                    node_list.append(nod.right)

            if any([n is not None for n in node_list]): # make sure counting the level has valid node
                ans = max(ans, len(node_list))

        return ans