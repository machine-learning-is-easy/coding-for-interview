
from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # convert banned to set
        banned = set(banned)

        # count the number of most frequent words
        def remove_punctuation(str):
            punctuation = """!?',;."""
            return ''.join([c if c not in punctuation else ' ' for c in str])

        no_punct_paragraph = remove_punctuation(paragraph.lower())

        freq = defaultdict(int)

        most_freq_token = None
        most_occr = 0
        for w in no_punct_paragraph.split():
            if w not in banned:
                freq[w] += 1
                if freq[w] > most_occr:
                    most_freq_token = w
                    most_occr = freq[w]
        return most_freq_token