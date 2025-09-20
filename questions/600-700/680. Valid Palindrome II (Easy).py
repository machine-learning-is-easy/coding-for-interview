

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<=j:
            if s[i]!=s[j]:
                snew=s[:i]+s[i+1:]
                snew2=s[:j]+s[j+1:]
                if snew==snew[::-1]:return True
                elif snew2==snew2[::-1]:return True
                else:
                    return False
            i+=1
            j-=1
        return True