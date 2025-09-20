
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        tries = dict()
        ans = set()

        for fol in folder:
            val = fol.split('/')[1:]
            curr = tries
            temp = '/'
            for v in val:
                if 'end' in curr:
                    break

                temp += v + '/'
                curr = curr.setdefault(v, {})

            curr['end'] = True
            ans.add(temp[:-1])

        return list(ans)

