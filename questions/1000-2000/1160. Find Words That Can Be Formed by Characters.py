

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        char_dict = Counter(chars)
        total_len = 0

        for w in words:
            w_dict = Counter(w)
            if all([char_dict[key] >= w_dict[key] if key in char_dict else False for key in w_dict]):
                total_len += len(w)
        return total_len