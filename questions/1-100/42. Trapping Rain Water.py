


class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        t = 0
        l = len(height)
        lm = [0] * l
        rm = [0] * l
        lm[0] = height[0]
        for i in range(1, l):
            lm[i] = max(height[i], lm[i - 1])

        rm[l - 1] = height[l - 1]
        for j in range(l - 2, -1, -1):
            rm[j] = max(height[j], rm[j + 1])

        for j in range(1, l - 1):
            t += min(lm[j], rm[j]) - height[j]

        return t


class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            if left_max < right_max: # left_max is lower
                left += 1
                water += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
            else: # right_max is lower
                right -= 1
                water += max(0, right_max - height[right])
                right_max = max(right_max, height[right])

        return water

        return water