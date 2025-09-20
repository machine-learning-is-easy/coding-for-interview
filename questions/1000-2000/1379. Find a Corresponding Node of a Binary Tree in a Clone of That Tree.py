

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(cloned)]
        while stack:
            n = stack.pop()
            if n.val == target.val: return n
            if n.left: stack.append(n.left)
            if n.right: stack.append(n.right)
                                                            #Recursive DFS
        if not original: return None
        return None