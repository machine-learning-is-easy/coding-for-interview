

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        sentence = sentence.split()
        for ind, word in enumerate(sentence):
            if word[0] in vowels:
                sentence[ind] = word + "ma" + "a" * (ind + 1)
            else:
                sentence[ind] = word[1:] + word[0] + "ma" + "a" * (ind + 1)

        return " ".join(sentence)