


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        force = 0
        for idx in range(0, n):
            if dominoes[idx] == "R":
                force = n
            elif dominoes[idx] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)

            forces[idx] = force

        for idx in range(n - 1, -1, -1):
            if dominoes[idx] == "L":
                force = n
            elif dominoes[idx] == "R":
                force = 0
            else:
                force = max(force - 1, 0)
            forces[idx] -= force

        res = ["."] * n
        for idx in range(n):
            if forces[idx] > 0:
                res[idx] = "R"
            elif forces[idx] < 0:
                res[idx] = "L"
        return "".join(res)
