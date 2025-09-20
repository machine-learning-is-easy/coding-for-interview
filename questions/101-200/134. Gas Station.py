

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if sum(gas) < sum(cost): return -1   #   Example: gas = [1,2,3,4,5]  cost = [3,4,5,1,2]
                                             #
        tank = idx = 0                       #   i  gas  cost   tank        start
                                             #  ––– –––  ––––   –––––––––   –––––
        for i in range(len(gas)):            #   start = 0              0     0
                                             #   0   1    3    0+1-3 = -2     1    reset tank to 0, start to 0+1 = 1
            tank+= gas[i]-cost[i]            #   1   2    4    0+2-4 = -2     2    reset tank to 0, start to 1+1 = 2
            if tank < 0: tank, idx = 0, i+1  #   2   3    5    0+3-5 = -2     3    reset tank to 0, start to 2+1 = 3
                                             #   3   4    1    0+4-1 =  3     3
        return idx
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
assert Solution().canCompleteCircuit(gas, cost) == 3