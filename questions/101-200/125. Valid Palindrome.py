

class Solution:
    def isPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while end > start and not s[end].isalnum():
                end -= 1

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1
        return True

# concise version
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        while left < right:
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            elif not s[right].isalnum():
                right -= 1
            elif not s[left].isalnum():
                left += 1
            else:
                return False

        return True