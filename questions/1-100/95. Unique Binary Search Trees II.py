


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def getTreeList(nodes):
            if not nodes:
                return [None]
            res = []
            for i, val in enumerate(nodes):
                for leftTree, rightTree in product(getTreeList(nodes[:i]), getTreeList(nodes[i + 1:])):
                    res += [TreeNode(val, left=leftTree, right=rightTree)]
            return res

        return getTreeList(tuple(range(1, n + 1)))