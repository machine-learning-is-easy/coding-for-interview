

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        from collections import defaultdict
        result = 0
        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)

        for num in nums1:
            hashmap1[num] = hashmap1[num] + 1

        for num in nums2:
            hashmap2[num * k] = hashmap2[num * k] + 1

        max_nums1 = max(nums1)

        for key2 in hashmap2:
            multiple = key2
            while multiple <= max_nums1:
                if multiple in hashmap1:
                    result = result + hashmap1[multiple] * hashmap2[key2]
                multiple = multiple + key2
        return result