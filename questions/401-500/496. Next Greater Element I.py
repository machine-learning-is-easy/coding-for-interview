

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # put the nums2 into dictionary
        num2_dict = {num:ind for ind, num in enumerate(nums2)}

        # find the next greater element of nums2
        nxt_great = [-1] * len(nums2)
        stack = []
        for ind, num in enumerate(nums2):
            while stack and nums2[stack[-1]] < num:
                nxt_great[stack.pop(-1)] = ind
            stack.append(ind)

        print(nxt_great)
        res = [0] * len(nums1)
        for ind, num in enumerate(nums1):
            if num in num2_dict:
                if nxt_great[num2_dict[num]] != -1:
                    res[ind] = nums2[nxt_great[num2_dict[num]]]
                else:
                    res[ind] = -1
        return res