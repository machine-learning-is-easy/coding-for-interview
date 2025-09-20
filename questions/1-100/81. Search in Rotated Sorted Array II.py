

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums) - 1
        if nums[start] == target or nums[end] == target:
            return True

        while start <= end:
            mid = int((start + end) / 2)
            if target == nums[mid]:
                return True

            if nums[start] == nums[mid]:
                start += 1
            elif nums[mid] == nums[end]:
                end -= 1
            elif nums[start] < nums[mid]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # 右半段有序
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return False