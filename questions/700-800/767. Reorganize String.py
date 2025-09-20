

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1

        sorted_chars = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)

        if freq_map[sorted_chars[0]] > (len(s) + 1) // 2:
            return ""

        res = [None] * len(s)

        i = 0
        for char in sorted_chars:
            for _ in range(freq_map[char]):
                if i >= len(s):
                    i = 1
                res[i] = char
                i += 2

        return "".join(res)