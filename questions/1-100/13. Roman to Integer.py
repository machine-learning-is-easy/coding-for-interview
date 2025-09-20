


class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for ind in range(len(s)):
            c = s[ind]
            if c in dict:
                value = dict[c]
                if c == 'I':
                    if ind + 1 < len(s) and s[ind + 1] in ["V", "X"]:
                        total -= value
                    else:
                        total += value

                elif c == 'X':
                    if ind + 1 < len(s) and s[ind + 1] in ["L", "C"]:
                        total -= value
                    else:
                        total += value

                elif c == 'C':
                    if ind + 1 < len(s) and s[ind + 1] in ["D", "M"]:
                        total -= value
                    else:
                        total += value
                else:
                    total += value
        return total
