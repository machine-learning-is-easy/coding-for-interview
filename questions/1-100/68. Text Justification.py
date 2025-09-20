

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        Result_list = []
        Str = words[0]
        for word in words[1:]:
            if (len(Str) + 1 + len(word) <= maxWidth):
                Str = Str + ' ' + word
            else:
                St = self.Justify(Str, maxWidth)
                Result_list.append(St)
                Str = word
        Result_list.append(Str + ' ' * (maxWidth - len(Str)))
        return Result_list

    def Justify(self, Str, maxWidth):
        word_list = Str.split()
        if len(word_list) == 1:
            return Str + ' ' * (maxWidth - len(Str))
        spaces = maxWidth - (len(Str) - (len(word_list) - 1))
        quo = int(spaces / (len(word_list) - 1))
        rem = spaces % (len(word_list) - 1)
        return (' ' * (quo + 1)).join(Str.split()[:rem + 1]) + ' ' * quo + (' ' * quo).join(Str.split()[rem + 1:])


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            # Determine how many words fit in this line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            line_words = words[i:j]
            spaces_needed = maxWidth - line_len
            gaps = j - i - 1

            # If it's the last line or only one word in the line
            if j == n or gaps == 0:
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            else:
                # Distribute spaces evenly
                space_per_gap = spaces_needed // gaps
                extra_spaces = spaces_needed % gaps

                line = ""
                for k in range(gaps):
                    line += line_words[k]
                    line += ' ' * (space_per_gap + (1 if k < extra_spaces else 0))
                line += line_words[-1]  # last word, no space after

            res.append(line)
            i = j

        return res