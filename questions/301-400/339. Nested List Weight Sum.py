

class Solution:
    def depthSum(self, nestedList):
        def sum_nest_list(nested_list, level):
            total = 0
            for item in nested_list:
                if isinstance(item, int):
                    total += item * level
                elif isinstance(item, list):
                    total += sum_nest_list(item, level + 1)
            return total

        return sum_nest_list(nestedList, 1)


assert Solution().depthSum([[1,1],2,[1,1]]) == 10