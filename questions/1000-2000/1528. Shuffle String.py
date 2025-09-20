

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        converted_list = [''] * len(s)
        for c, ind in zip(s, indices):
            converted_list[ind] = c

        return ''.join(converted_list)
