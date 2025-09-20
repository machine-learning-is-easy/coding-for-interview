# two sum. You need to find two numbers in nums that add up to target and return their indices.
"""
Common Approaches
1. Brute-force
Loop over all pairs of numbers and check if they sum to target.
Time complexity: O(n²)
Space complexity: O(1)

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
2. Hash Table / Dictionary (Optimal)

Use a dictionary to store numbers and their indices as you iterate.
For each number num, check if target - num exists in the dictionary.
Time complexity: O(n)
Space complexity: O(n)

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]