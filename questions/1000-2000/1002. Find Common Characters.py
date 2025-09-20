


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        # commen_token = set([w for w in words[0]])
        counter_word0 = Counter(words[0])

        for word in words[1:]:
            counter_word = Counter(word)

            for key in list(counter_word0.keys()):
                if key not in counter_word:
                    del counter_word0[key]
                else:
                    counter_word0[key] = min(counter_word0[key], counter_word[key])
        # reorganise the return

        res = []
        for key in counter_word0:
            res += [key] * counter_word0[key]
        return res

