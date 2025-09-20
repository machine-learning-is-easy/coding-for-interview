# List
---
## Key points:
### 1.1	The left array and right array contain the most water, like 27. Remove duplicate elements.
### 1.2	Continuous sum arrays like 523, iteration from left to right, if the sum is negative, start a new counting.
### 1.3	Put the element to the visited hash table like 167 and split the array into two arrays. 
### 1.4	Hash table: can save the remaining selection in the hash table with keys and values.
### 1.5	Is there a 0 in the array? (Typical questions for 3 sum). Return all combinations or just return true or false.
### 1.6	Put numbers into a hash table to record the index of the element.
### 1.7	Next permutation is a special case. Step 1 find the first element i which is not decreasing order from end to start of the array, step 2, find the first element which is greater than value of I from the right elements of index I (the minimum value of the values which is greater than index I in the right portion of index i), and swap two values. Step 3. Reverse all the elements after index i.
### 1.8	Repeating checking a list or stack. 2297 jump III, 75. Sort Colors.
### 1.9	Interval merge
### Topology sorting (next greater value)
---
## Questions:
###  Are the elements ordered?

### Does the array include a duplicate element? (if duplicates, select different index elements are treated as different scenarios)
### Does allowing select the same element multiple times?
### The element number is variable or not? Like sum to 0 questions, 2, 3 or 4?
### Any negative element in the array?
### Are 0s in the array?

## a.	Hash table
### 1)	Quick sort
```python
def partition(start, end, array):
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:

        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < end and array[start] <= pivot:  # not guarantee array[start] > pivot
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if (start < end):
            array[start], array[end] = array[end], array[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # Returning end pointer to divide the array into 2
    # possible end < start (not necessary start = end).
    # why return end (end position is guarantee array[end] is not > arra[pivot_index])
    # arr[start] may > pivot. we cannot put the start value to the pivot index, because, we want left half <= pivot
    return end


# The main function that implements QuickSort
def quick_sort(start, end, array):
    if (start < end):
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)

        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
```

### 2)	Two sums
Clarify: 
#### 1.	Ask if the array is sorted or not. Does the array have duplicate elements or not? Return is all the possible solution or any solution. If sorted, can use two pointers, if not sorted and there are no duplicate elements, need to push the element to a set and check the residual.
#### Duplicate elements? (Override of dictionary keys, if still want to use a dictionary, need to set the value of the key to list)
Can select the same element twice?
Including 0?

#### 2.	Can select the same number multiple times?
Tip: The hash table records the element index, and iteration over the array, if target -current value in the hash table, return the value of the hash table [target-current value], otherwise, add the current value to the hash table, and the value is the index.

### 167. Two Sum II - Input Array Is Sorted: 

### 15. Three sums
questions: does the list include duplicate elements? They are different when.
The list needs to be ordered, if not ordered, needs ordered first, if the array is ordered, the left and right pointer works. Otherwise, need a backtracking algorithm to solve it
Pay attention if the array includes duplicate elements. If include a duplicate element, when finding the solution, need to move the left pointer to the right to find the next not same value element.

If allow select element multiple times or not. If yes, need the left to start from the first loop index, and left <= right in the while loop. 

N sums or any possible combination of elements to a target
TIP: if no fixed number of elements, should use the backtracking algorithm, if the number is more than three
Extended question 4 sums, 5 sums (need to use backtracking to solve this problem)

### 454. 4Sum II
TIPS: put two sums into the hash table and count the number of the sum. Iteration the other two sums, check if the 0 – num3[i] – num4[i] is in the hash table. If yes count the sum. 

## 3)	Sum less than K
1099. Two Sum Less Than K
Sort the array and two pointers moving to left and moving right.

## 4)	The closest three sums to the target
Question: continuous three elements?
### 16. 3sum closest
Questions: 1. Can select multiple times? 2. Can the elements in the array be the same? 3. Does the array contain three elements sum equal to the target? 4. What is the return value, can be positive or distance? 5. continuous three elements?
TIPS: keep a record of the distance to the target while searching three sums to the target. Others are the same. Iteration over the array and searching two elements of the rest of the array.

If it is an ordered array and requires a consecutive 3 numbers. Can use a binary search to search.

### 259. 3Sum Smaller
TIPS: sorting the array. Iteration from left to right. When fixing one value, left (ind + 1) and right pointer (end of the array) to the elements on the right of the fixed index. When find the sum of three elements is less than the target. Res += r – l (which is total number of sum less than the target). then move left pointer to right. If three sum > target, move right to left.
```python
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        #choose three elements from the array, and the order doesn't matter, and beause our gaol is to find something related to the sum, so in the first step, sort in
        nums.sort()
        res = 0
        for i in range(len(nums)-2):
            #find the number of result when the first element of the triplet is nums[i]
            l,r = i+1, len(nums)-1
            #use two pointer as the second and end point of the triplet
            while l < r:
                if nums[i]+nums[l]+nums[r] < target:
                    #if nums[i]+nums[l]+nums[r] < target, then r-1,r-2...r-(r-l-1) all satisfy the rrequirement
                    res += r-l
                    #all the possible cases when the middle element has the index of l are considered
                    l += 1
                else:
                    #if nums[i]+nums[l]+nums[r] < target, then l+1, l+2..l+(r-l-1) are all not available, so all cases with r are considered
                    r -= 1
        return res
```

## 5)	Continuous sum
### 523. Continuous Subarray Sum. 
Tips: don’t forget to add 0:0 in the first place (the sub-array starts with 0) and add mode residue in a hash table. Two index value deduction mod K will equal the same mod. Because this question requires a minimum of two numbers, so need to keep the index of the element, and compare the current element sum is greater than the potential element index + 1
### 525. Contiguous Array
Accumulative sum of the 0 and 1. If 1 increase one, if 0 decrease one. the result into dictionary d, Put the value is the accumulative sum, and the value is the index. If the accumulative sum in the dictionary.  The equal length of 0 and 1 are current index - d[acc]

### 134. Gas Station
TIPS: continuous sum of cost and gas, if the sum is lower than 0, start a new index and tank

### 1331. Rank Transform of an Array
TIPS: sort the array and put the number into a hash table. The value is the index in the sorted array. In the original array, we can get the right order index to replace the original value.

### 2365. Task Scheduler II
TIPS: the solution is similar to continuous sum. Put the maximum day for each key. Go through the first to the end. If the days >= than the maximum days. Process the task. Otherwise wait until to the task maximum day. 
```python
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:

        start_day = {task: 0 for task in tasks}
        day = 0
        for task in tasks:
            day += 1

            # if the current day is too early to complete the task,
            # fast forward the day to the earliest day you can.
            if day < start_day[task]:
                day = start_day[task]

                # update the earliest day you can complete the task.
            start_day[task] = day + space + 1

        return day
```

## 6)	Number of combinations to target (element can be used multiple times? not constraint on number of elements)
A very important issue is if all elements are greater than 0 or not.
### 377. Combination Sum IV
Tips: the list element can be repeated. Save the intermediate target into a hash table (only if the element cannot repeat, could not use a hash table to store intermediate result or use @lru_cache annotation function). Recursive function but not backtracking. The memo does not record the path, it saves the temporal result which is a different path. Backtracking pops the path. This question is classic if want to save the intermediate number to a hash table.
```python

class Solution:
    def combinationSum4(self, nums, target):
        memo = {} # only the elments of nums can be repeated selected. if not repeated, could not use memo

        def combine(nums,target,memo):
            if target==0:
                return 1
            if target < 0:
                return 0
            res=0
            if target in memo:
                return memo[target]

            for item in nums:
                a = combine(nums, target-item, memo)
                res += a

            memo[target]=res
            return res

        return combine(nums, target, memo)

```
## 7)	Number of combinations to target (element can only be used once)
### 40. Combination Sum II
if the element can be selected only once and needs to save the result, needs backtracking to solve it.
TIPS: backtracking to search over the entire array. keep a record of the current index, and iteration over from the current index to the end of the array, once the array is to the temp array, recursive to call (index+1, candidate, temp, target-candidate[index]). We could not use the hash table to save the intermediate result as 377. Combination Sum IV

If it starts with index + 1. That is a combination, if starts with 0, that is a permutation.

What about the lower number of elements sum to the target? we sort the array in non-increasing order and select from the largest number to the lowest number.

Another solution is sorting the array, and skip the same element in the backtracking process
```python
class Solution:
    def combinationSum2(self, candidates, target: int):

        result = []
        candidates.sort()
        def backtrack(start, candidates, temp, target):

            if target == 0:
                result.append(list(temp))
                return

            for i in range(start, len(candidates)):
                # already traversed i - 1, if i and i-1 are the same, not necessary to traverse i
                # it require the array to be sorted.
                if i > start and (candidates[i] == candidates[i - 1]):
                    continue
                temp.append(candidates[i])

                if target - candidates[i] >= 0:
                    backtrack(i + 1, candidates, temp, target - candidates[i]) # need start from i + 1
                temp.pop()

        backtrack(0, candidates, [], target)
        return result


```

## 8)	number of continuous arrays to reach the target.
### 560. Subarray Sum Equals K. Tips: the first element of the accumulation array needs to be 0. Put the previous value into a HashMap key. And value of the keys needs to be times of accumulation value appears. Pay attention to the value of keys in the hash table can be more than 1. Add {0:0} into the accumulation array.
### 1218. Longest Arithmetic Subsequence of Given Difference.
TIPS: iteration from the left to right. 
```python

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        map = {}
        for val in arr:
            map[val] = map.get(val - difference, 0) + 1
        return max(map.values())

```
## 9)	Intersection two array
### 349. Intersection of Two Arrays
Are two arrays sorted or not?

Tips: put one array in a hash table by counter, then iterate over the other array, if find an element in the hash table and the value of the key is > 0, put it into the result, decrease the key to the hash table - 1.
Questions: pay attention if the array has a duplicate element, if yes, need to keep the number of the element, if put one element in the result, need the number -1. If do not have a duplicate element, only need to check if the second array element is in the dict.
## 10)	Convert the list to a set.
### 128. Longest Consecutive Sequence
TIPS: convert the list into a hash table, iteration over the list, if the element + 1 in the set length + 1. Also need to put the seen element into another element, if already count an element, pass it.
Optimization tips: cache the length of the findings.

### 939. Minimum Area Rectangle
TIPS: the idea is for a given point x1, y1. searching for other points (x1, y2), (x2, y2), (x2, y1). To get all the points from x, and y, need to convert the (x, y) points into a dictionary x_axis and y_axis. And put the points tuple into a hashtable. 

### 836. Rectangle Overlap


## 11)	724. Find Pivot Index
TIPS: left and right value. Left value is 0. The right value is sum of the array. Index move from left to right. At each index, left value plus the nums[ind-1], the right value minus the nums[ind]. Until the two values are equal.
```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left_val = 0
        right_val = sum(nums)
        ind = 0
        while ind < len(nums):
            right_val -= nums[ind]
            if ind > 0:
                left_val += nums[ind - 1]
            if left_val == right_val:
                return ind
            ind += 1
        return -1

```

### 239. Sliding Window Maximum
```python

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        st = []
        res = []

        for i in range(k):
            heapq.heappush(st, (-nums[i], i))

        res.append(-st[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(st, (-nums[i], i))
            while st[0][1] <= i - k:
                heapq.heappop(st)
            res.append(-st[0][0])

        return res

```
### 480. Sliding Window Median ******

Two heaps to sort the min and max value of the interval. Check the new element and old element, to modify the min and max heap. 
```python
class Solution:
    # TC - O((n - k)*log(k))
    # SC - O(k)
    # 121 ms, faster than 96.23%

    def find_median(self, max_heap, min_heap, heap_size):
        if heap_size % 2 == 1:
            return -max_heap[0]
        else:
            return (-max_heap[0] + min_heap[0]) / 2

    def medianSlidingWindow(self, nums, k: int):
        max_heap = []
        min_heap = []
        heap_dict = defaultdict(int)
        result = []

        for i in range(k):
            heappush(max_heap, -nums[i])
            heappush(min_heap, -heappop(max_heap))
            if len(min_heap) > len(max_heap):
                heappush(max_heap, -heappop(min_heap))

        median = self.find_median(max_heap, min_heap, k)
        result.append(median)

        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            heap_dict[prev_num] += 1

            balance = -1 if prev_num <= median else 1

            if nums[i] <= median:
                balance += 1
                heappush(max_heap, -nums[i])
            else:
                balance -= 1
                heappush(min_heap, nums[i])

            if balance < 0:
                heappush(max_heap, -heappop(min_heap))
            elif balance > 0:
                heappush(min_heap, -heappop(max_heap))

            # only pop the first element which are not in the K interval.
            while max_heap and heap_dict[-max_heap[0]] > 0:
                heap_dict[-max_heap[0]] -= 1
                heappop(max_heap)

            while min_heap and heap_dict[min_heap[0]] > 0:
                heap_dict[min_heap[0]] -= 1
                heappop(min_heap)

            median = self.find_median(max_heap, min_heap, k)
            result.append(median)

        return result

```

### 97. Interleaving String (need to switch parameter)
Tips: a long string can be composed of a letter b and a letter of a. Use recursive matching of a long string to verify if the long string can be composed of the first letter of s1 or the first letter of s2. Then convert the long string to a shorter string and recursively call itself.
If the question is changed to a long string composed of s1 and s2 alternatively, that means the long string can be composed of one letter from a and one letter from b alternatively. The recursive function will be called with the exchange of the parameters of s1 and s2. (Put residual string as a parameter in the recursive function/backtracking)

Attention: If exactly requires one letter from s1 and the other from s2, when calling the recursive function, need to exchange the parameters of s1 and s2.
```python

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        def matching_string(s1, s2, long_str):
            # this is a typical recursive function in string matching
            if not s1 and not s2 and not long_str:
                return True
            elif long_str:
                if s1 and s2:
                    # one letter can comes from s1 or comes from s2
                    return (s1[0] == long_str[0] and matching_string(s1[1:], s2, long_str[1:])) or (
                                s2[0] == long_str[0] and matching_string(s1, s2[1:], long_str[1:]))
                elif s1:
                    return s1[0] == long_str[0] and matching_string(s1[1:], s2, long_str[1:])
                elif s2:
                    return s2[0] == long_str[0] and matching_string(s1, s2[1:], long_str[1:])
                else:
                    return False

            else:
                return False

        return matching_string(s1, s2, s3) or matching_string(s2, s1, s3)

```
### 1004. Max Consecutive Ones III
TIPS:  keep the sliding window with k zeros. The variable I is the tail, J is the head.  J moves right counting zeros, when zero number > k, move i to right until the zero count = k. Calculate the length of j – i + 1
```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        maxi = 0
        j = 0
        zero = 0
        while j < len(nums):
            if nums[j] == 0:
                zero += 1

            while zero > k:
                if nums[i] == 0:
                    zero -= 1
                i += 1

            if zero <= k:
                maxi = max(maxi, j - i + 1)
            j += 1
        return maxi

```
### 387. First Unique Character in a String
TIPS: put the last index of the character in a dictionary. Then from left to right check if every character index == dictionary[char]
### 1207. Unique Number of Occurrences

### 2405. Optimal Partition of String

## b.	Stack
### 1911. Maximum Alternating Subsequence Sum
Tips: make the odd num as low as possible, keep the even num as high as possible, and pop the last even num (kind of greed algorithm)
Even index is positive, the odd index is negative, from start to the end put all elements into an array, if the length of the array is even, the last element will be negative. The current element will be positive if add current value to the array, then compare the last element of the array with the current element, if the current element is less than the last element of the array, then pop the last element (make the negative number be smaller), if the length of the array is odd, last element will be positive, compare the current value with last element, if the current value is greater than last element, pop last element (make the positive number greater)

### 1209. Remove All Adjacent Duplicates in String II
TIPS: push element to a stack, and check if last k element is the same.
### 20. Valid Parentheses
Push bracket into a stack. If encounter right bracket, check if the top of the stack is relevant left bracket, if yes pop last element, else return False

### 247. Strobogrammatic Number II
TIPS: five numbers can be used “0”, “1”, “8”, “6” and “9”. If the length is odd. Need to start with “0”, “1”, “8”. If the length is even, need to start with the empty string “”.  One step appends one letter at the beginning and one corresponding digit at the end. Increase the length by two.
BFS search is better, while steps < n: pop all the element, for each element key + s + v, and append the new string to the queue. step + 2.

### 227. Basic Calculator II
Save the operator before each number, iteration from left to right, if find a operator, refresh the operator with new operator, if find a digit, loop the next digit, until to find all digit. Then try to push the number to the stack, it depends on the operator, if operator is +, put the number into the stack directly, if -, put -number into the stack, if *, pop the last element, then times current number and add the result into the stack, if /, pop the last element, then divide the current number and add the result into the stack.

### 1047. Remove All Adjacent Duplicates In String

## c.	Merge list
Questions: can any node be None?
1)	Merge two sorted arrays
Tips: iteration from the end to the beginning 
2)	Merge K list
Tips: get the min from the list one time and link the node to the head

### 2007. Find Original Array From Doubled Array
Question: are all values positive?
TIPS: pay attention to 0. 2*0 = 0. The tip is converting the original array into a hash table, the value is how many times of key is in the array. Sort the changed list from low to high. 
Iteration over the sorted array, find the element, decrease the value of the key in the array (remove current value from the hash table). Then check the 2*key in the hash table and the 2*key value is greater than 0, if yes, decrease the value of 2*key by 1. Add the current key to the result list. The most important is to remove the element while iteration over the array.

What is there are negative elements? Need to sort on abs(value)

## d.	Left and right value
### 42. Trapping Rain Water
Tip: Get left max, right max, and current height
2)	Partition Array into Disjoint Interval.
### 915. Partition Array into Disjoint Intervals
Tips: Find the left max value (including current index), and right min value (not including current index).  If an index left max value < right min value (index + 1). Then split the array into left and right sections. Pay attention to return current index + 1
### 1762. Buildings with an Ocean View.
### 670. Maximum Swap
Tips: right maximum index variation. Keep the maximum left number index from right to the left including the current index.
### 633. Sum of Square Numbers
Need to keep the array sorted.
Can select the same element?
Tips: two-pointer variations. Left pointer, right pointer, if sum of squares greater than the target, move left pointer to right, else move right point left.

### 697. Degree of an Array (find the minimum contiguous length of subarray which has the same degree)
Find the left first seen and right first seen of maximum frequency numbers, the return is minimum of right_first_seen – left_first_seen + 1 of all maximum frequency numbers.

### 926. Flip String to Monotone Increasing

Tips: the minimum flip is min (flip left 1 to 0 and flip right 0 to 1, flip all to 1, flip all to 0)
Define left_1 and right_0 arrays with the same length as the original array.
Iteration over the original array, count the number of 1s, and assign the value to the left_1 array. Iteration over the original array from right to left, count the number of 0s, and assign the value of 0 to the right_0 array.
Iteration over left_0 and right_0 array, get minimum of left_0 + right_0. 
Return the minimum of min (res, max(right_0), max(left_1))

### 845. Longest Mountain in Array
TIPS: Similar with 941. Valid Mountain Array. 941 is using left and right point searching from left and right. 845 is fix the top of the hill searching from left and to right.

Alternative: if the element is not necessary consecutively. Need to run montonic stack from left to right and find the longest uphill value. And run monotonic stack from right to left. then find the longest downhill value. When adding the longest uphill value and the downhill value, it will be the longest hill value

### 2334. Subarray With Elements Greater Than Varying Threshold

### 849. Maximize Distance to Closest Person
For each index, find the distance to the closest 1 on its left, and find the distance to the closest 1 on its right. The maximum distance is a minimum of two distances.
Create left_1 array and right_1 array. 
Iteration over the array from left to right, for each index find the closest 1

### 283. Move zeros
Question: do we need to keep the original sequence of the non-zero item?
If need to keep the non-zero in the original sequence: iteration over the num list from left to right. When encountering a zero element, pop this element and append it at the end. And count the zeros +1. Until the index reaches length of nums array – zeros numbers.

### 2256. Minimum Average Difference
TIPS: left sum right sum, iteration from left to right. The left sum increases, right sum decreases. Get the average from left and right sum and length.

### 1991. Find the Middle Index in Array
TIPS: similar to 2256. Left sum and right sum. When moving right, the left sum increases and the right sum decreases.

### 895. Maximum Frequency Stack
# question, if pop a value, does this value will be remove from the stack of lower frequency of the value still exist in the stack.
TIPS: freq: dict of key and value is the number of the key pushed to the stack. Group: dict save the the ith pushed to the stack. And keep the maximum of the key.  When pushing a value to the stack, increase the value repetition + 1. Push the value to the repetition + 1 list. Check the maximum_freq value. 
When pop a value. Get the maximum_freq value, pop the value, and check if the the maximum_freq has value, if not decrease maximum_freq
class FreqStack:
```python


    def __init__(self):
        self.freq = defaultdict(int)
        self.groups = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > self.maxFreq: self.maxFreq = self.freq[val]
        self.groups[self.freq[val]].append(val)

    def pop(self) -> int:
        first = self.groups[self.maxFreq].pop(-1)
        self.freq[first] -= 1
        if not self.groups[self.maxFreq]:
            self.maxFreq -= 1

        return first
```

### 905. Sort Array By Parity
TIPS: move even to the right and odd to the left. Left and right pointer. If left is odd, switch left and right value, move right to left by 1, else move left to right by 1 until left = right

### 611. Valid Triangle Number ???
```python

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()
        ans = 0
        for k in range(len(nums) - 1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans

```
## e.	Sort list
### 27. Remove Element
Left and right pointer, if right pointer value is equal to the value move right pointer to left. if not, check the left pointer, if left pointer not equal to the value, more left pointer to the right. If the left pointer value is equal to the value, that means right pointer is not equal to the value, left pointer value is equal to the value, exchange the left pointer value and the right pointer value, move left pointer to right and move right pointer to the left.

### 75. Sort Colors
Three-pointer, start, cur and end. End pointers save the biggest one, start pointers save the smallest one, cur moves from left to the end when encountering the smallest switch with left, increase left and cur points. when encountering the biggest one switch with the end pointer only. 
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = curr = 0
        # for all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
```

### 334. Increasing Triplet Subsequence
TIPS: find there triplet (num[i], num[j], num[k]), I < j < k and num[i] < num[j] < num[k] three pointers: 
```python

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
```

## f.	jump
Max jump
Tips: define an array of min jump steps. The first element is 0. Start from the first element, from the current step, the current value steps, Calculate the steps of the next cells jump steps from the current cell, save the min for jumps from the current index and the value of step of the jumps for the next cells.

Reachable jump
### 45. Jump Game II
### 55. Jump Game

### 1306. Jump Game III
TIPS:
```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        def dfs(ind):
            nonlocal visited
            if arr[ind] == 0:
                return True
            else:
                visited.add(ind)
                for nxt_ind in (ind - arr[ind], ind + arr[ind]):
                    if 0 <= nxt_ind < len(arr) and nxt_ind not in visited:
                        if dfs(nxt_ind):
                            return True
                visited.remove(ind)
            return False

        return dfs(start)
```

### 2297. Jump Game VIII
Need to use monotonic stack and repeating check the element of the stack.

## g.	Two pointers
### 11. Container with Most Water.
Tips: left and right pointer. If the left pointer is smaller move the right, if the right pointer is smaller, move the right pointer to the left.

### 1868. Product of Two Run-Length Encoded Arrays
TIPS: find minimum frequency, add (value, mini_frequence) to the result. Be careful, need to check if the last element of the result list is the same value, and merge the new to the last element. Next, update the next element.

``` python
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
```

### 977. Squares of a Sorted Array
TIPS: left and right pointer to the beginning and the end of the array. Select the max of left and right pointer values, put the higher value to the end of the result array. Then move the left or the right pointer. 

### 1539. Kth Missing Positive Number
TIPS: one pointer t is the array index starting from 0, other pointer c is starting from 1, compare the array[t] to c, if equal, move bother pointer to next, otherwise, decrease k, move c. until exhaust all element, return array[-1] + k

### 415. Add Strings

## h.	KLargest
1)	Find KLargest element in an array.
Tips, not sort but use minimum heap, minimum heap keeps the minimum element at the root. When getting a number higher than the root element, replace the root element and heapify the root. The time complexity is logK.

Get K largest value, we can heapify the list and get k element from the 0 index, then heapify the rest element will get the top K largest.

### 973. K Closest Points to Origin:
TIPS: using max heap to store the K closest Points when iteration over the position list.
When encountering a point whose distance is closer to the first element, replace the first element with a new point and distance, heapify the list.
The trick is heapq.heapify is min heap. If we want to keep the k closest point, we need to put the maximum distance to the first position. Need to -1 * distance.

Import heapq
Heapq.heapify(a): convert a to min heap, if want maximum heap, convert the element to -1* distance
class MedianFinder:
```python

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num):
        heappush(self.small, -num)
        heappush(self.large, -heappop(self.small))

        if len(self.small) < len(self.large):
            heappush(self.small, -heappop(self.large))

    def findMedian(self):
        if len(self.large) != len(self.small):
            return -self.small[0]
        else:
            return (self.large[0] - self.small[0]) / 2
```

## i.	Find Median from Data Stream
### 1)	295. Find Median from Data Stream
TIPS: set the minimum heap and maximum heap

## j.	Stack (validate the parentheses)
TIPS: there are three brackets. Round bracket, square bracket, and curly bracket. All those brackets should appear in pairs.
Check if the string follows some rules
### 20. Valid Parentheses: https://leetcode.com/problems/valid-parentheses/
Tips, encounter the left bracket (round, box, curly), push it to stack, encounter the right bracket check if the top of the stack is the same type of left bracket, if yes, pop the top of the stack, if no return false.
### 394. Decode String
TIPS: digit stack, string stack. If encounter a digit, continue the digit checking, until find all the digits, and put the digit into the digit stack. It can put multiple-digit numbers into the stack. If encounter “]”, pop the string stack and digit stack, multiply them and add the result to the last of the string stack. 
pay attention digit, the digit can be multiple digits. Also, the compound bracket.
```python

class Solution:
    def decodeString(self, s: str) -> str:
        # ***********
        left = 0
        stack = [""]
        num_stack = []
        while left < len(s):
            if s[left].isdigit():
                digit = ""
                # Convert the string to int as it can double digits
                while s[left].isdigit():
                    digit += s[left]
                    left += 1

                digit_int = int(digit)
                stack.append("")
                num_stack.append(digit_int)
            elif s[left] == ']':
                mul_string = num_stack.pop()
                top_str = stack.pop()
                stack[-1] += mul_string * top_str
            else:
                stack[-1] += s[left]
            left += 1

        return stack[0]
```
### 1249. Minimum Remove to Make Valid Parentheses: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
TIPS: use a stack to track the bracket pairs. The string list to record the changed strings.
What if it has multiple parentheses like [], {}, (). We can use DFS to remove one and get the minimum.
Alternative: keep a list left_bracket only save (, when encounter ), check if left_bracket is empty, current ) is invalid, remove current ). After finishing all the elements check, the remaining left_bracket is the illegal right_bracket. The question can ask the minimum step of changes to make valid parentheses, the minimum step is swap the left bracket and right bracket + delete the bracket. min(left_bracket, right_bracket) + abs(left_bracket – right_bracket)
```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        stack = []
	# count the illegal )
        for i, c in enumerate(s_list):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    s_list[i] = ''

        # count illegal (
        while stack:
            s_list[stack.pop()] = ''
        
        return "".join(s_list)
```
### 1190. Reverse Substrings Between Each Pair of Parentheses

### 921. Minimum Add to Make Parentheses Valid. 
Check the length of the stack.

### 856. Score of Parentheses
TIPS: instead of keeping records of the bracket, push the score to the stack.
```python

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                v = stack.pop(-1)
                stack[-1] += max(2 * v, 1)
        return stack.pop(-1)
```
### 241. Different Ways to Add Parentheses
TIPS: for every operator, the operator may be the very last operator. Recursive call left half string and right half string. After getting the left half possible result and right half possible result. Permute the operation and generate all possible result. Return all possible results.
```python
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Define a function to calculate the result of the given operator between two numbers
        def calc(left, right, operator):
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right

        # Define the main function to calculate all possible results
        def diffWaysToComputeHelper(inputStr):

            # If the input string only has digits, return a list with that number
            if inputStr.isdigit():
                return [int(inputStr)]

            # Initialize the output list
            outputList = []

            # Iterate through each character of the input string and check if it is an operator or not
            for i in range(len(inputStr)):
                if inputStr[i] in ['+', '-', '*']:

                    # Recursively call the `diffWaysToCompute()` function for the left and right substrings of the operator
                    leftResults = diffWaysToComputeHelper(inputStr[:i])
                    rightResults = diffWaysToComputeHelper(inputStr[i + 1:])

                    # Combine the results using the operator
                    for left in leftResults:
                        for right in rightResults:
                            outputList.append(calc(left, right, inputStr[i]))

            # Return the output list
            return outputList

        # Call the helper function
        return diffWaysToComputeHelper(inputStr)
```

### 1190. Reverse Substrings Between Each Pair of Parentheses
TIPS: Using a stack to store all the characters, if see a “)”, pop up the last element until to see a “(”, concatenate the popped character (converse the string in the bracket). Then push the string in the stack from the beginning to the end (reverse sequence). Repeat the process, until the last character in the string. Return the joined characters in the stack with an empty string.

### 1021. Remove Outermost Parentheses
TIPS: count the left and right bracket. Cnt + 1 when encounter (, -1 when encounter). Add (to the result if cnt > 0 and add ) to the result when cnt > 1.
```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans, cnt = [], 0
        for ch in s:
            if ch == '(' and cnt > 0:
                ans.append(ch)
            if ch == ')' and cnt > 1:
                ans.append(ch)
            if ch == "(":
                cnt += 1
            else:
                cnt -= 1

        return "".join(ans)
```
### 1963. Minimum Number of Swaps to Make the String Balanced
TIPS: find the orphan bracket [ and]. The total number is N, and the maximum swap is ceil(N//2/2)
```python

class Solution:
    def minSwaps(self, s: str) -> int:

        stack = []
        for p in s:
            if p == "[":
                stack.append(p)
            else:
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(p)

        orphan = len(stack) // 2
        return ceil(orphan / 2)
```
### 678. Valid Parenthesis String
TIPS: try to match the right bracket. Remove the matched right bracket. Then match the left bracket with stars. Need to add index to left bracket stack and ast
```python

class Solution:
    def checkValidString(self, s: str) -> bool:
        left, ast = [], []

        for i, char in enumerate(s):
            if char == "(":
                left.append(i)
            elif char == "*":
                ast.append(i)

            # The next three conditions are when char == ")"
            elif left:  # Match left paren with right paren
                left.pop()
            elif ast:  # Match asterix with right paren
                ast.pop()
            else:  # Can't match this right paren with anything
                return False

            # Found matches for all right parens, now match any leftover left parens
            # Ensure any asterix used as a right paren comes after the left paren we are matching
        while left and ast and left[-1] < ast[-1]:
            left.pop()
            ast.pop()

        # If there's any leftover left parens, then we couldn't match those, so False
        return not left
```
### 1614. Maximum Nesting Depth of the Parentheses
TIPS: encounter (, plus 1, encounter) minus 1. Keep the maximum of the number.

### 32. Longest Valid Parentheses
TIPS: put the index into the stack instead of putting the bracket into the stack
```python

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stck = [-1]  # initialize with a start index
        for i in range(len(s)):
            if s[i] == '(':
                stck.append(i)
            else:
                end = stck.pop()  # the poped ")", the stack is empty
                if stck:  # we do have previous index value
                    if s[end] == "(":  # current ) is valid, do a calculation
                        max_length = max(max_length, i - stck[-1])  # update the length of the valid substring
                    else:  # current ) is not valid, add the current index to the stack and start a new calculation
                        stck.append(i)
                else:
                    stck.append(i) # start a new calculation

        return max_length
```
### 1598. Crawler Log Folder
TIPS: if encounter ../ pop a path, else push a path. Return len(stack)

## k.	Monotonic stack
TIPS: iteration over the list or linked list, put the value into a stack and repeatedly check the top of the stack element value is less than the current value, if yes, pop the top element until the top element value is larger than the current value. Calculate the rectangle area.

### 84. Largest Rectangle in Histogram
TIPS: it is tricky to calculate the height and width. iteration from left to right. Put all the elements index to a stack. In each loop, if the current element is less than stack top element, need to calculate the previous height area. The width is current index - previous stack index -1. The height is the stack top element height. 

### 503. Next Greater Element II
TIPS: run twice of the monotonic stack

### 1475. Final Prices with a Special Discount in a Shop
TIPS: run monotonic stack

### 402. Remove K Digits
TIPS: Run monotonic stack. 
```python

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = list()
        for n in num:
            while st and k and st[-1] > n:
                st.pop()
                k -= 1

            if st or n is not '0':  # prevent leading zeros
                st.append(n)

        if k:  # not fully spent, remove element less than k
            st = st[0:-k]

        return ''.join(st) or '0' # think about if all element are removed
```
need to take care of the situation where monotonic stack pop less than K

### 496. Next Greater Element I
TIPS: put nums2 into a dictionary. Find the next greater element of nums2. Then iteration of nums1, find the index of nums2 and find the index next greater element. Be careful decreasing stack is saving the index other than the value.
```python

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
```
### 2487. Remove Nodes From Linked List
TIPS: monotonic stack plus linked list operation. Put all the nodes into the monotonic stack and remove previous node which value is less than next nodes. Then pop all the nodes from the stack and connect the nodes into a linked list.
### 739. Daily Temperatures
Similar with next greater element.

## l.	Monotonic queue
### 862. Shortest Subarray with Sum at Least K *****
TIPS: increasing queue
```python
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)

        deque = collections.deque()
        result = float(inf)
        for i, sum_ in enumerate(pre):
 		  # remove the sum higher than current sum
            while (deque and deque[-1][1] >= sum_):
                deque.pop()

 		  # remove the longest sum which length > k
            while deque and sum_ - deque[0][1] >= k:
                result = min(i - deque[0][0], result)
                deque.popleft()

            deque.append([i, sum_])
        return result if result != float(inf) else -1
```
Alternative:
Create the cumulative sum of the array, iteration the accumulative sum of the array, put the element to a dictionary, the key is the index, the value is the accumulative sum, for each iteration, get the value of the  

## m.	Consecutive sequence
### 152. Maximum Product Subarray.py. 
Question: do the elements need to be consecutive? Can the element be 0? Can the input be an empty array? What is the return of an empty array?
Tips: keep min_so_far and max_so_far during iteration of the whole array

### 1186. Maximum Subarray Sum with One Deletion *******
```python

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        maxOneDel= [-1e10 for i in range(0, len(arr))]
        maxNoDel = [-1e10 for i in range(0, len(arr))]
        maxNoDel[0] = maxOneDel[0] = res = arr[0]

        for idx in range(1, len(arr)):
            maxNoDel[idx] = max(maxNoDel[idx - 1] + arr[idx], arr[idx])
            maxOneDel[idx] = max(maxNoDel[idx-1], maxOneDel[idx-1] + arr[idx])
            res = max(res, max(maxNoDel[idx], maxOneDel[idx]))

        return res
```
## n.	Normal iteration
### 26. Remove Duplicates from Sorted Array: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Tips: iteration from the start of the array, when encountering a current element equal element before current element, pop current element. (This is only allowing the appearance times more than two)

### 540. Single Element in a Sorted Array
TIPS: the array is sorted is very important. if not sorted, we can use a hash table. If sorted, we can iterate over the array, if encounter an element whose next element is not the same as the current. 

## o.	Simulation

### 723. Candy Crush
TIPS: 1. While true in the outer loop until reaches stable condition. Check horizontal and vertical crush, add the crushable cell into a set. Then set the crushable set with 0. Last is moving the 0 cells downward. Iteration from the bottom row. Check upwards cell, if upward cell is 0, offset plus one. If the upside cell is not empty, move [row][col] to [row + offset] [col]. And assign [row][col] with 0

### 1823. Find the Winner of the Circular Game
```python
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [ind + 1 for ind in range(n)]
        ind = 0
        while len(friends) > 1:
            # count k
            for _ in range(1, k):
                ind += 1
            ind = ind % len(friends)
            friends.pop(ind)
        return friends[0]
```
## p.	Convert to dictionary.
### 2342. Max Sum of a Pair With Equal Sum of Digits
TIPS: Put the number into keys of the sum of digits of the number

### 649. Dota2 Senate
TIPS: two queues, one queue is for Radian and the other is for Dire. Run until Radiant or Dire is empty. 
Pop two element, if index of radian is lower than dire, append radian back to radian queue.
```python

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)
        return "Radiant" if radiant else "Dire"
```

## q.	String concatenation
### 2023. Number of Pairs of Strings With Concatenation Equal to Target

## r.	Increasing order
### 1909. Remove One Element to Make the Array Strictly Increasing
TIPS: for each one nums[i] < nums[i-1], there are two possible solution, remove nums[i-1], and remove[i]. if remove nums[i-1], no operation, need to make record has encounter one violate the rule. If remove nums[i], if nums[i] < nums[i-2], need nums[i] = nums[i-1] for next iteration. Continue to the next iteration, if encounter next nums[i] < nums[i-1] return False.
```python

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed_once = False
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                if removed_once:
                    # the second time to see a lower value.
                    return False
                if i > 1 and nums[i] <= nums[i - 2]:
                    # remove i
                    nums[i] = nums[i - 1]
                # the first delete.
                removed_once = True
        return True
```
### 665. Non-decreasing Array
TIPS: attention nums[i] = nums[i-1] to remove element i.
```python

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        num_violations = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if num_violations == 1:
                    return False
                num_violations += 1
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

        return True
```
## s.	Math expression
### 150. Evaluate Reverse Polish Notation
TIPS: using stack to store numbers. When encounter operator, pop two elements, do the operation, add the result to the stack.

## t.	Next permutation
### 31. Next Permutation

### 528. Random Pick with Weight