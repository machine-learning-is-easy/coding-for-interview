

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = Counter(s)
        arr = []

        for ch in counter:
            if counter[ch] % 2:
                counter[ch] -= 1
                arr.append(ch)
            if len(arr) > 1:
                return []

        def permute(arr, counter, res):
            if len(arr) == n:
                res.append("".join(arr))

            for ch in counter:
                if counter[ch] == 0:
                    continue
                counter[ch] -= 2
                permute([ch] + arr + [ch], counter, res)
                counter[ch] += 2

        res = []
        n = len(s)
        permute(arr, counter, res)

        return res