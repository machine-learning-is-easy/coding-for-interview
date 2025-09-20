

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        _string = ""

        def rserialize(root):
            """ a recursive helper function for the serialize() function."""
            # check base case
            nonlocal _string
            if root is None:
                _string += 'None,'
            else:
                _string += str(root.val)
                _string += ','
                rserialize(root.left)
                rserialize(root.right)

        rserialize(root)
        return _string

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l.pop(0))
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))