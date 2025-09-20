

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_str = "0123456789abcdef"
        result = ""
        num &= 0xFFFFFFFF
        while num > 0:
            result = hex_str[num & 0XF] + result
            num >>= 4
        return result