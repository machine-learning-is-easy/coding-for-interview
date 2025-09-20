

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        """
        ["with","example","science"]

        "thehat"

        """
        N = len(target)
        letdic = defaultdict(list)
        tset = set(target)

        for stick in stickers:
            ls = [l for l in stick if l in tset]
            for l in ls:
                letdic[l].append(ls)

        q = [(0, len(target), list(target))]  # need to be a list to save all letters, including the duplicate letters
        # if asking the minimum type of stickers, can use set().

        while q:
            used, lent, targ = heapq.heappop(q)

            if targ[0] not in letdic.keys(): return -1

            for wrd in letdic[targ[0]]:
                newtarg = targ[:]
                for lw in wrd:
                    if lw in newtarg:
                        newtarg.remove(lw)
                if not newtarg:
                    return used + 1
                heapq.heappush(q, (used + 1, len(newtarg), newtarg))

        return -1