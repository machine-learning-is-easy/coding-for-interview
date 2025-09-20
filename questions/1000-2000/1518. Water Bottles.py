
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        total_number = 0

        full_bottles = numBottles
        empty_bottle = 0
        while full_bottles > 0:
            total_number += full_bottles
            empty_bottle += full_bottles

            full_bottles = empty_bottle // numExchange
            empty_bottle = empty_bottle % numExchange

        return total_number
