
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        d = collections.defaultdict(int)
        stack = []
        for i, c in enumerate(s):
            if c == "(": stack.append(i)
            if c == ")": d[stack.pop()] = i

        def get_tree(l: int, r: int) -> Optional[TreeNode]:
            if l > r: return None

            val = []
            while l <= r and s[l] != "(":
                val.append(s[l])
                l += 1
            node = TreeNode(int("".join(val)))
            if l >= r: return node

            left_l_p = l
            left_r_p = d[left_l_p]
            node.left = get_tree(left_l_p + 1, left_r_p - 1)

            right_l_p = left_r_p + 1
            right_r_p = d[right_l_p]
            node.right = get_tree(right_l_p + 1, right_r_p - 1)

            return node

        return get_tree(0, len(s) - 1)
