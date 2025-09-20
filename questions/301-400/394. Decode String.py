

class Solution:
    def decodeString(self, s: str) -> str:
        # ***********
        left = 0
        stack = [""]
        num_stack = []
        while left < len(s):
            if s[left].isdigit():
                digit = ""
                # Convert the string to int as it can double digits
                while s[left].isdigit():
                    digit += s[left]
                    left += 1

                digit_int = int(digit)
                stack.append("")
                num_stack.append(digit_int)
            elif s[left] == ']':
                mul_string = num_stack.pop()
                top_str = stack.pop()
                stack[-1] += mul_string * top_str
            else:
                stack[-1] += s[left]
            left += 1

        return stack[0]

assert Solution().decodeString("3[a]2[bc]") == 'aaabcbc'


class Solution:
    def decodeString(self, s: str) -> str:
        left = 0
        res = [""]
        num_stack = []

        while left < len(s):
            if s[left].isdigit():
                right = left
                while s[right].isdigit():
                    right += 1
                num = int(s[left:right])
                num_stack.append(num)
                left = right
                continue
            elif s[left] == "[":
                res.append("")
            elif s[left] == "]":
                top_string = res.pop(-1)
                num = num_stack.pop(-1)
                res[-1] += top_string * num
            else:
                res[-1] += s[left]
            left += 1
        return res[0]
assert Solution().decodeString("3[a]2[bc]") == 'aaabcbc'