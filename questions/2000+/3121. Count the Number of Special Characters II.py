

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_ind = dict()
        # put all the letter in a dict
        # record the last index of lower case character, first index of lower case character
        for idx, l in enumerate(word):
            if l.islower():
                first_ind[l] = idx
            else:
                if l not in first_ind:
                    first_ind[l] = idx

        count = 0
        count_l = set()
        for l in word:
            if l.lower() in first_ind and l.upper() in first_ind and first_ind[l.lower()] < first_ind[l.upper()]:
                if l.lower() not in count_l:
                    count += 1
                    count_l.add(l.lower())
        return count
