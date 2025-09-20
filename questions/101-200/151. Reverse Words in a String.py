

class Solution:
    def reverseWords(self, s: str) -> str:
        list_str = s.split()
        list_str.reverse()
        return " ".join(list_str)