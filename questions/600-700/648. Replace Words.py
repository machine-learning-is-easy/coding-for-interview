

class TireNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False


class Tire:
    def __init__(self):
        self.root = TireNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TireNode()
            cur = cur.children[char]
        cur.endOfWord = True


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tire = Tire()
        for root in dictionary:
            tire.insert(root)

        words = sentence.split(' ')
        res = []
        for word in words:
            cur = tire.root
            temp = ''
            prefix_exist_in_d = False
            for char in word:
                # Case1: found root of the word in the tire, break out early
                if cur.endOfWord:
                    prefix_exist_in_d = True
                    break
                if char in cur.children:
                    temp += char
                    cur = cur.children[char]
                # Case 2: if the char is not in the tire, directly break out
                else:
                    break

            # Case3: the word exactly exist in the tire
            if cur.endOfWord:
                prefix_exist_in_d = True

            # Depend on above 3 cases, decide on what to add in the list
            if not temp or not prefix_exist_in_d:
                res.append(word)
            elif temp and prefix_exist_in_d:
                res.append(temp)

        return ' '.join(res)