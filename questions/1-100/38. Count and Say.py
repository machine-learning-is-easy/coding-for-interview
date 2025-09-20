
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        # Get the previous term in the sequence
        prev = self.countAndSay(n - 1)

        result = ""
        count = 1

        # Loop through the string and apply run-length encoding
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result += str(count) + prev[i - 1]
                count = 1
        # Add the last group
        result += str(count) + prev[-1]

        return result