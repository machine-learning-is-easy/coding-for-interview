


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occ = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                # this is checking the last element of the stack. if last element of the stack
                # has duplicates, and current letter < last element, should remove the letter.
                while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)

        return ''.join(stack)


s = "bcabc"
assert Solution().removeDuplicateLetters(s) == "abc"