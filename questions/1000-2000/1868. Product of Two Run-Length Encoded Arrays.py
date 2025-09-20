

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        if not encoded1 or not encoded2:
            return []

        e1 = 0
        e2 = 0
        cur_num1, cur_freq1 = encoded1[0]
        cur_num2, cur_freq2 = encoded2[0]

        res = []
        while cur_freq1 and cur_freq2:

            product = cur_num1 * cur_num2

            # print(f'product:{product}')
            # print(f'cur_num1:{cur_num1}, cur_freq1:{cur_freq1}, cur_num2: {cur_num2},cur_freq2:{cur_freq2}')
            min_freq = min(cur_freq1, cur_freq2)
            cur_freq1 -= min_freq
            cur_freq2 -= min_freq

            if not res or res[-1][0] != product:
                res.append([product, min_freq])
            else:
                pre_product, pre_freq = res[-1]
                res[-1] = [pre_product, pre_freq + min_freq]

            # update next element
            if cur_freq1 == 0 and e1 <= len(encoded1) - 2:
                e1 += 1
                cur_num1, cur_freq1 = encoded1[e1]

            if cur_freq2 == 0 and e2 <= len(encoded2) - 2:
                e2 += 1
                cur_num2, cur_freq2 = encoded2[e2]

        return res