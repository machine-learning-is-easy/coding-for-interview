

"""
find the the path of the target node (in the path all the child nodes can be saved). put the path into a list. BFS search the target node to right and left, search 
other nodes when the distance is less than k.
"""


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # (find_node, distance)
        # edge case on root and target
        if not root:
            return []

        res = []

        def find_nodes(node, depth):
            if not node:
                return

            if depth >= 0:
                if node.val not in res and depth == 0 and node.val not in visited:
                    res.append(node.val)
                visited.add(node.val)
                find_nodes(node.right, depth - 1)
                find_nodes(node.left, depth - 1)
            else:
                return

        path = []

        def find_path(node, tmp):
            nonlocal path
            nonlocal target
            if not node:
                return
            tmp.append(node)
            if node.val == target.val:
                path = list(tmp)
            else:
                find_path(node.left, tmp)
                find_path(node.right, tmp)
            tmp.pop(-1)

        find_path(root, [])
        step = 0
        visited = set()
        while path:
            node = path.pop(-1)
            find_nodes(node, k - step)
            step += 1
        return res