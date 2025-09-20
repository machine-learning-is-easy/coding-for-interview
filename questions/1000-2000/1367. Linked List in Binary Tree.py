
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        d=deque()
        d.append(root)
        def dfs(node1,node2):
            if not node2:
                return True
            if not node1 or node1.val!=node2.val:
                return False
            return dfs(node1.right,node2.next) or dfs(node1.left,node2.next)
        while(d):
            for _ in range(len(d)):
                curr=d.popleft()
                if curr.val==head.val and dfs(curr,head):
                    return True
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
        return False