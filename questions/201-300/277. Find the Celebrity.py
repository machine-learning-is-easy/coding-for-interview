

class Solution:
    def findCelebrity(self, n: int) -> int:
        # define the hashtable. key is the person be known, the value is how many people know the person
        celeb = 0
        for i in range(n):
            if knows(celeb, i):
                celeb = i

        for i in range(n):
            if (knows(celeb, i) and celeb != i) or not knows(i, celeb):
                return -1

        return celeb