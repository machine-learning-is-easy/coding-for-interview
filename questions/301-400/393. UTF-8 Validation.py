

class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        # the UTF8 is at most 4 bytes long
        # so the first bit is at most 4 1

        count = 0  # count # of byte remaining

        for num in data:

            if count == 0:
                if bin(num >> 5) == '0b110':
                    count = 1
                elif bin(num >> 4) == '0b1110':
                    count = 2
                elif bin(num >> 3) == '0b11110':
                    count = 3
                elif bin(num >> 7) == '0b1':
                    return False  # other wise, you need to be 1 byte, which first bit start with 0.

            else:
                if bin(num >> 6) != '0b10': return False
                count -= 1

        return count == 0
