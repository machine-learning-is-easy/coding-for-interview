

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Where to write next compressed char
        left = 0   # Start of current group

        for right in range(len(chars)):
            # Check if end of group or end of array
            if right + 1 == len(chars) or chars[right] != chars[right + 1]:
                chars[write] = chars[left]
                write += 1
                count = right - left + 1
                if count > 1:
                    for c in str(count):
                        chars[write] = c
                        write += 1
                left = right + 1  # Move to next group

        return write