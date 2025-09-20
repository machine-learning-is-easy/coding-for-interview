

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for letter in columnTitle:
            digit = ord(letter) - ord("A") + 1
            ans = ans * 26 + digit

        return ans