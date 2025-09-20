

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strings:
            key = ()
            for i in range(len(s) - 1):
                circular_difference = 26 + ord(s[i+1]) - ord(s[i])
                key += (circular_difference % 26,)
            hashmap[key] = hashmap.get(key, []) + [s]
        return list(hashmap.values())


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashtable = defaultdict(list)

        for s in strings:
            key = ()
            for idx in range(len(s) - 1):
                differnece = 26 + ord(s[idx + 1]) - ord(s[idx])
                key += (differnece % 26,)

            hashtable[key] += [s]
        return list(hashtable.values())