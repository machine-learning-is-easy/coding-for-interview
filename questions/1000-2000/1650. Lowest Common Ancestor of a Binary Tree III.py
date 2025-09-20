


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # get parent node from p
        p_parent = set()

        bottom = p
        while bottom:
            p_parent.add(id(bottom))
            bottom = bottom.parent

        bottom = q
        while bottom:
            if id(bottom) in p_parent:
                return bottom
            else:
                bottom = bottom.parent
