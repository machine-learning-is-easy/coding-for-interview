

# breath first search
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        digit_list = [c for c in digits]
        if digits == '':
            return []
        queue = [""]
        for c in digit_list:
            for _ in range(len(queue)):
                sub_str = queue.pop(0)
                chars = phone[c]
                for c_ch in chars:
                    queue.append(sub_str + c_ch)
        return queue