
class Solution:
    def checkValidString(self, s: str) -> bool:
        left, ast = [], []

        for i, char in enumerate(s):
            if char == "(":
                left.append(i)
            elif char == "*":
                ast.append(i)

            # The next three conditions are when char == ")"
            elif left:  # Match left paren with right paren
                left.pop()
            elif ast:  # Match asterix with right paren
                ast.pop()
            else:  # Can't match this right paren with anything
                return False

            # Found matches for all right parens, now match any leftover left parens
            # Ensure any asterix used as a right paren comes after the left paren we are matching
        while left and ast and left[-1] < ast[-1]:
            left.pop()
            ast.pop()

        # If there's any leftover left parens, then we couldn't match those, so False
        return not left