
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(index: int, path: str):
            if index == len(s):
                result.append(path)
                return

            if s[index].isalpha():
                # Explore both lowercase and uppercase
                backtrack(index + 1, path + s[index].lower())
                backtrack(index + 1, path + s[index].upper())
            else:
                # Just continue with the digit
                backtrack(index + 1, path + s[index])

        backtrack(0, "")
        return result