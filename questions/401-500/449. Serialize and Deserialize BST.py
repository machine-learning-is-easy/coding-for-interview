

class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """

        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []

        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """

        def helper(lower=float('-inf'), upper=float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None

            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root

        data = [int(x) for x in data.split(' ') if x]
        return helper()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans