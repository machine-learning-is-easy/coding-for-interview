
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Calculate the sum of all numbers in the array
        nums_sum = sum(nums)
        # If the sum cannot be evenly divided by k, it is not possible
        if nums_sum % k != 0:
            return False

        # Calculate the target sum for each subset
        target_sum = nums_sum // k
        # Sort the array in descending order to optimize pruning
        nums.sort(reverse=True)
        # Keep track of which numbers have been used in subsets
        used = [False] * len(nums)

        # Depth-first search function to explore all possible subsets
        def dfs(sub_sets_count, cur_sum, start_index):
            # If we have found k subsets, it is a valid partition
            if sub_sets_count == k:
                return True
            # If the current subset sum matches the target sum, move to the next subset
            if cur_sum == target_sum:
                return dfs(sub_sets_count + 1, 0, 0)

            # Iterate through the remaining numbers in the array
            for i in range(start_index, len(nums)):
                # If the number has been used or adding it exceeds the target sum, skip it
                if used[i] or cur_sum + nums[i] > target_sum:
                    continue

                # Pruning step: if the current number is the same as the previous number
                # and the previous number hasn't been used, skip the current number
                if i > start_index and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # Mark the current number as used
                used[i] = True
                # Recursive call to explore the next number and update the subset sum
                if dfs(sub_sets_count, cur_sum + nums[i], i + 1):
                    return True
                # Undo the choice of using the current number and try the next number in the array
                used[i] = False

            # If no solution is found, return False
            return False

        # Start the depth-first search from the beginning of the array with an empty subset
        return dfs(0, 0, 0)