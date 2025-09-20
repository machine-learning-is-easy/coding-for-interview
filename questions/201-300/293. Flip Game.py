

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:

        res = []

        def change_onestep(str_, p):
            # is str string, p is position
            if len(str_[p:]) >= 2:
                if str_[p:p + 2] == "++":
                    res.append(str_[:p] + "--" + str_[p + 2:])
                    change_onestep(str_, p + 1)
                else:
                    change_onestep(str_, p + 1)

        change_onestep(currentState, 0)

        return res
