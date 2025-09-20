
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []  # Stack to maintain the current path of nodes
        i = 0  # Pointer for parsing the string

        while i < len(traversal):
            depth = 0
            # Count the number of dashes to determine depth
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1

            # Extract the node value
            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1

            # Create the new node
            node = TreeNode(value)

            # If depth equals the stack size, it means this is the left child
            while len(stack) > depth:
                stack.pop()

            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            # Push the current node to stack
            stack.append(node)

        # The root of the tree is the first element in the stack
        return stack[0]
