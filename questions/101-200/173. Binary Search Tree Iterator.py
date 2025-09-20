
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.traversal = list()
        self.index = 0
        self._inOrderTraversal(root)

    def next(self) -> int:
        if self.hasNext():
            tmp = self.traversal[self.index]
            self.index += 1
            return tmp

    def hasNext(self) -> bool:
        return (self.index + 1) <= len(self.traversal)

    def _inOrderTraversal(self, subroot: TreeNode):
        if subroot == None:
            return

        self._inOrderTraversal(subroot.left)
        self.traversal.append(subroot.val)
        self._inOrderTraversal(subroot.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.iter = self._inorder(root)
        self.nxt = next(self.iter, None)

    def _inorder(self, node: Optional[TreeNode]) -> Generator[int, None, None]:
        if node:
            yield from self._inorder(node.left)
            yield node.val
            yield from self._inorder(node.right)

    def next(self) -> int:
        res, self.nxt = self.nxt, next(self.iter, None)
        return res

    def hasNext(self) -> bool:
        return self.nxt is not None

