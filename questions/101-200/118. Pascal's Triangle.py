
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        queue = [[1]]
        for _ in range(numRows):
            l = queue.pop(0)
            res.append(l)
            new_l = [1]
            if len(l) >= 2:
                ind = 0
                while ind < len(l) - 1:
                    new_l.append(l[ind] + l[ind + 1])
                    ind += 1
            new_l.append(1)
            queue.append(new_l)

        return res