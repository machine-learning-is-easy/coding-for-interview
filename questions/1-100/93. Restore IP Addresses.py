


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        if len(s) > 12:
            return res

        def dfs(i, dots, curip):
            if i == len(s) and dots == 4:
                res.append(curip[:-1])  # to remove the fourth dot - [:-1]
                return

            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j + 1]) <= 255 and (i == j or s[i] != "0"):  # allow .0. but not allow .01.
                    dfs(j + 1, dots + 1, curip + s[i:j + 1] + ".")

        dfs(0, 0, "")
        return res