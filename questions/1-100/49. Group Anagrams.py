

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using set as key of a dict
        d = dict()
        for w in strs:
            cl = [c for c in w]
            cl.sort(key=lambda a:a)
            k = ''.join(cl)
            if k in d:
                d[k].append(w)
            else:
                d[k] = [w]
        return [[w for w in d[k]] for k in d.keys()]