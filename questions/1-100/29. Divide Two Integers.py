


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        a = abs(dividend)
        b = abs(divisor)

        negative = (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0)

        output = 0

        while a >= b:
            counter = 1
            decrement = b

            while a >= decrement:
                a -= decrement

                output += counter
                counter += counter
                decrement += decrement

        output = output if not negative else -output

        return min(max(-2147483648, output), 2147483647)
# time complexity is O((log a)^2)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge case for overflow
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        # Determine the sign of the quotient
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Subtracting using bitwise shifting to speed up the process
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        # Apply the sign
        return -quotient if negative else quotient