
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        path_collection = []

        def path(node, string):
            nonlocal path_collection
            if node is None:
                path_collection.append(string)
            else:
                if node != root:
                    string += "->"
                string += str(node.val)
                if node.left and node.right:
                    path(node.left, string)
                    path(node.right, string)
                elif node.left:
                    path(node.left, string)
                elif node.right:
                    path(node.right, string)
                else:
                    path_collection.append(string)

        path(root, '')
        return path_collection
