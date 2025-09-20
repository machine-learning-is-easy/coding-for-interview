

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:

        res = []

        def dfs(node):
            if not node:
                return
            else:
                dfs(node.getNext())
                res.append(node.printValue())

        dfs(head)
        return res