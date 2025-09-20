


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:

        compound = [(s, t, ind) for s, t, ind in zip(sources, targets, indexes)]
        compound.sort(key=lambda x: x[2], reverse=True)
        tmp = S
        for s, t, ind in compound:
            if tmp[ind: ind + len(s)] == s:
                tmp = tmp[:ind] + t + tmp[ind + len(s):]
        return tmp

