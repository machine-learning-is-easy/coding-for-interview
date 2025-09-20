

class Solution:
    def sortSentence(self, s: str) -> str:
        s_split = s.split()

        res_s = [None for _ in range(len(s_split))]
        print(res_s)
        for word in s_split:
            digit=0
            ind = len(word) - 1
            while word[ind].isdigit():
                digit = digit * 10 + int(word[ind])
                ind -= 1
            print(digit)
            res_s[digit - 1] = word[:ind + 1]
        return ' '.join(res_s)