

# question, need to clear the question if the rectangle height is minimum height of the bar in the rectangle or
# Is the height of rectangle the minimum of the start bar and end bar.
class Solution:
    def largestRectangleArea(self, heights) -> int:
        ## RC ##
        ## APPROACH : MONOTONOUS INCREASING STACK ##
        ## Similar to Leetcode: 1475. Final Prices With a Special Discount in a Shop ##
        ## Similar to Leetcode: 907. Sum Of Subarray Minimums ##
        ## Similar to Leetcode: 85. maximum Rectangle ##
        ## Similar to Leetcode: 402. Remove K Digits ##
        ## Similar to Leetcode: 456. 132 Pattern ##
        ## Similar to Leetcode: 1063. Number Of Valid Subarrays ##
        ## Similar to Leetcode: 739. Daily Temperatures ##
        ## Similar to Leetcode: 1019. Next Greater Node In LinkedList ##

        ## LOGIC ##
        ## 1. Before Solving this problem, go through Monotone stack.
        ## 2. Using Monotone Stack we can solve 1) Next Greater Element 2) Next Smaller Element 3) Prev Greater Element 4) Prev Smaller Element
        ## 3. Using 'NSE' Monotone Stack concept, we can find width of rectangles, height obviously will be the minimum of those. Thus we can calculate the area
        ## 4. As we are using NSE concept, adding 0 to the end, will make sure that stack is EMPTY at the end. ( so all the areas can be calculated while popping )

        heights.append(0)
        stack = [-1]  # represent the last element 0.
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(ans, height * width)
            stack.append(i)
        heights.pop()
        return ans


class Solution:
    def largestRectangleArea(self, heights) -> int:
        # need to put 0 at the beginning of the list, 0 can not be popped as it is lowest.
        heights = [0] + heights + [0]
        stack = [0]  # represent the last element 0.
        ans = 0
        for i in range(len(heights)):
            # always pop the element if the stack element is higher than current value,
            # the stack elements are in increasing order.
            # if current value is lower than stack top value, calculate the height,
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(ans, height * width)
            stack.append(i)
        # heights.pop()
        return ans


heights = [2,1,5,6,2,3]
assert Solution().largestRectangleArea(heights) == 10