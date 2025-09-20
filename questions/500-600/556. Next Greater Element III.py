
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)

        # Step 1: Find first decreasing element from right
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i == -1:
            return -1  # Digits are in descending order

        # Step 2: Find next bigger digit on the right of i
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Step 3: Swap
        digits[i], digits[j] = digits[j], digits[i]

        # Step 4: Reverse the tail
        digits[i+1:] = reversed(digits[i+1:])

        # Step 5: Convert back to integer
        result = int(''.join(digits))

        # Step 6: Check 32-bit int range
        return result if result <= 2**31 - 1 else -1