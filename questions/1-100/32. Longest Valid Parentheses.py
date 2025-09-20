

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stck = [-1]  # initialize with a start index
        for i in range(len(s)):
            if s[i] == '(':
                stck.append(i)
            else:
                end = stck.pop()  # if popped ")" or popped -1 the stack is empty
                if not stck:  # if popped -1, or popped ), the stack is empty, it is not valid parentheses, add a new start index
                    stck.append(i)  #
                else:
                    if s[end] == "(":
                        max_length = max(max_length, i-stck[-1]) # update the length of the valid substring
        return max_length


# a better understanding coding.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stck = [-1]  # initialize with a start index
        for i in range(len(s)):
            if s[i] == '(':
                stck.append(i)
            else:
                end = stck.pop()  # the poped ")", the stack is empty
                if stck:  # we do have previous index value
                    if s[end] == "(":  # current ) is valid, do a calculation
                        max_length = max(max_length, i - stck[-1])  # update the length of the valid substring
                    else:  # current ) is not valid, add the current index to the stack and start a new calculation
                        stck.append(i)
                else:
                    stck.append(i) # start a new calculation

        return max_length

s = ")()())"
assert Solution().longestValidParentheses(s) == 4

