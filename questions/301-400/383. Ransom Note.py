


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine_dict = Counter(magazine)
        for s in ransomNote:
            if s in magazine_dict:
                magazine_dict[s] -= 1
                if magazine_dict[s] == 0:
                    del magazine_dict[s]

            else:
                return False
        return True