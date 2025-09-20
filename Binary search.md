#Binary search
----
## Keynotes:
### a)	Find the target, if the target is between the right-mid. Shift left =mid + 1, else shift right = mid -1.
### b)	If duplicate elements: shift left, and right conditions vary. Mid.value < target, move left to mid + 1. Mid.value >= target, move right to mid-1, then the left index is the first element of the target value in the array.
### c)	Finding the peak value. The condition can be arr[mid] < arr[mid+1] for peak value. 
### d)	Find the K closest to the element. The criterion is to find the span [array[mid], array [mid + K-1]], and compare the array[mid] and array [mid + K -1]. If distance(array[mid], target) > distance (array[mid + k -1], target), L = mid + 1. Else R = mid. while the condition is L < R. for example 658. Edge case: target < arr[0] and target > arr[-1]
### e)	The shift of the left and right can be -1. Like left = left -1 and right = right – 1. Actually, it is not a binary search anymore and the time complexity is O(n).
### f)	Matrix binary search. 

Linearly scanning the sorted array for low and high indices is highly inefficient since our array size can be in millions. Instead, we will use a slightly modified binary search to find the low and high indices of a given key. We need to do a binary search twice:
•	Once for finding the low index.
•	Once for finding the high index.
The outer loop is low <= high.
### Low index
Let’s look at the algorithm for finding the low index:
•	At every step, consider the array between low and high indices and calculate the mid index.
•	If the element at mid index is less than the key, low becomes mid + 1 (to move towards the start of the range).
•	If the element at mid is greater or equal to the key, the high becomes mid - 1. Index at the low remains the same.
•	When low is greater than high, low would be pointing to the first occurrence of the key.
•	If the element at low does not match the key, return -1.

### High index
Similarly, we can find the high index by slightly modifying the above condition:
•	Switch the low index to mid + 1 when the element at the mid index is less than or equal to the key.
•	Switch the high index to mid - 1 when the element at mid is greater than the key.

### Pay attention to left = mid + 1 and right = mid – 1, loop condition is left <= right, return value is left + 1
### 1.1.	Binary search
Time complexity is O(log(N)).
Tips: define left, right, in the loop of condition left <=right, find the mid, and follow rules to update left and right. Left = mid + 1 or right = mid -1. -1 is necessary, otherwise, it may end up with a dead loop. Return left (which should be right + 1)
### 1)	Normal search
Power(n)
### 2)	Find the peak.
### 4. Find the median of two array
TIPS: 1. Search the index of the first array, then calculate the index of the second array. The while loop condition is L <= R. 2. Find the left L1 and right R1 value of the first array and L2 and R2 for the second array. 3. The stop criterion is L1 <=R2 and L2<=R1. Return the value of (max(L1, L2), min(R1, R2))/2 for even total number of two arrays, or return the value max(L1, L2) for odd number total number of two arrays.
```python

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # put nums1 and nums2 into
        def getLeft(nums, partition):
            if partition <= 0:
                return -math.inf
            return nums[partition - 1]

        def getRight(nums, partition):
            if partition >= len(nums):
                return math.inf
            return nums[partition]

        n1 = len(nums1)
        n2 = len(nums2)

        # Binary Search Parameters(searching the shorter array)
        lo = 0
        hi = n1
        totalLength = n1 + n2

        while lo <= hi:
            partX = int((lo + hi) / 2)   # middle of array 1
            partY = int((totalLength + 1) / 2) - partX  # Middle of array 2

            l1 = getLeft(nums1, partX)  # number on the left of the partition - array 1
            r1 = getRight(nums1, partX)  # number on the right of the partition - array 1

            l2 = getLeft(nums2, partY)  # number on the left of the partition - array 2
            r2 = getRight(nums2, partY)  # number on the right of the partition - array 2

            # if the number on the left in array 1 is lesser than the number of on the right
            # of array 2 and the number on the left in array 2 is less than the number on
            # the right in array 1 then the correct partitions are found.

            if l1 <= r2 and l2 <= r1:

                # if the resulting array has even no of elements.
                if totalLength % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0

                # odd number of elements
                return max(l1, l2)

            # if left number in array 1 is higher than the right number in array 2.
            if (l1 > r2):
                # move the higher end to the left
                hi = partX - 1

            # if left number in array 2 is higher than the right number in array 1.
            if l2 > r1:
                # move the lower end to the right
                lo = partX + 1

        # incorrect result
        return -1
```
### 35. Search Insert Position
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            # the condition is very important, if out of the loop, nums[l] is the first element which is greater than target
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:  # end of the loop, nums[r] will be the first element which less than the target
                r = mid - 1
            else:
                return mid

        return l
```
### 162. Find Peak Element
Binary Search, Once required o(logn), needs to be binary search. The condition is nums[mid] vs nums[mid + 1]
```python

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def search(nums: List[int], l: int, r: int) -> int:
            if l == r:
                return l
            mid = int((l + r) / 2)
            if (nums[mid] > nums[mid + 1]): # mid + 1 has to lower than 
                return search(nums, l, mid)
            else:
                return search(nums, mid + 1, r)

        return search(nums, 0, len(nums) - 1)
```
updates of L and R are tricky. If nums[mid] > nums[mid + 1]), we see the mid value is greater than mid + 1, r = mid. Else which means nums[ind] <= nums[mid + 1], we need to assign l = mid + 1. 
Also, compare mid and mid + 1, don’t care if mid + 1 is greater than r.

Different from the common binary search update strategy which is l = mid +1, r = mid – 1. And current question does not compare L and R values. Only need to compare mid with mid + 1

3)	Find min and max index (ultimate version of binary search)
Compare the condition of the loop with quicksort.

## 1.2.	2D binary Search
### 74. Search a 2D Matrix: 
TIPS:  start from the top right as a pivotal index, if the pivotal index value is greater, current column values are all greater than the search value. Move the column to the left. If the pivotal index value is lower, if all current row is less than the search value moves the row down. (it is required the row and column are ordered)

TIPS: two binary searches. Row binary search and column binary search.  For row binary search, if row[0] <= target < row[-1], continue the column binary search. Else move left or right pointer.

### 240. Search a 2D Matrix II
TIPS: Treat the 2D matrix as a 1D array. traditional binary search on the 1D array, if n is row number and m is the column. search starts from 0 to m*n - 1. Find the middle index, the element will be [mid //m][mid %m] (this is required the 2D matrix elements are fully ordered) the difference with 74 is if the matrix is sorted by rows and columns or by all elements

## 1.3.	Square root
Does X > 1?  If 0<x<1, the searching area is [0, 1] not [0, x]

### 69. Sqrt(x). 
Tips: L, R point to 1 to x, find middle m, if m* m > x, move left, else move right. Until to find the right m which is m * m == x

### 1.4.	Power n
Is N an integer?
Tips: power(n), keep base and exponent, exponent mod 2, if equal 1, multiple results with base, base equal base times base. Exponent equals exponent floor divided 2. Return the result (binary search)
 
## 1.5.	Find interval.
### 34. Find the First and Last Position of the Element in the Sorted Array
Tips: end = mid – 1, start = mid + 1, loop condition is start <= end
Two binary searches. The first condition is arr[mid] < target: then left = mid + 1, else right = mid – 1 (find the very first left element index). The second condition is arr[mid] <= target, then left = mid + 1, else right = mid -1 (find the very first right element index)

## 1.6.	Rotated array
### 81. Search in Rotated Sorted Array II (Medium)
KEYPOINTS:
#### 1.	allow duplicate, first to check if mid == start (start += 1) or mid == end (end -= 1)
#### 2.	mid > start, if target between (start, mid), end = mid -1. Else: start = mid + 1
#### 3.	mid < start, (mid, end) is ordered, if target is between (mid, end), start = mid + 1, else end = mid – 1

TIPS: binary search the entire array, set the start and end to 0 and length – 1. Update start and end in a while loop. Find the middle point. 
if the mid > start, the left half is ordered, if the middle is between start and mid, update end to mid–1. Otherwise, update starts with mid-1. Else mid < start, the right half is ordered. If the target is between mid and end value, update the start with mid + 1, otherwise, update the end with mid – 1. 
If mid == start, start += 1

### 33. Search in Rotated Sorted Array (with distinct values, no duplicated)
```python

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while start <= end:

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[start]: # becarefule >=
                # left side is in order
                if target < nums[mid] and target >= nums[start]: # be careful >=
                    end = mid - 1 # be carefule -1
                else:
                    start = mid + 1

            else:
                # right side is in order
                if target > nums[mid] and target <= nums[end]: # be carefule <=
                    start = mid + 1
                else:
                    end = mid - 1

        return -1
```
### 153. Find Minimum in Rotated Sorted Array
Question: if duplicate numbers are in the array. If duplicate numbers are allowed, need to L += 1 if nums[L] == nums[mid] or R-=1 if nums[R] == nums[mid]. The iteration is always L=mid +1 and R = mid – 1. Otherwise, it is probabily endless loop. Record the minimum of the array min_val = min(min_val, nums[R], nums[L], nums[mid]). We can optimize the condition later.

### 154. Find Minimum in Rotated Sorted Array II (Medium)
The tricky thing is allowing duplicate numbers
TIPS:
#### 1.	Because of allowing duplicate numbers in the array, need to check if left == mid and right == mid, if left == mid. Left +=1. If right == mid, right += 1, in the next loop avoids the duplicate numbers
#### 2.	Because of binary search, l = mid + 1 or r = mid – 1. Need to keep a record of minimum. Because mid -1 or mid +1 is not necessarily the lowest.
#### 3.	When left == mid, left += 1, when right == mid, right -= 1
#### 4.	If move left, minimum = min (left, minimum), if move right, minimum = min (right, minimum)

TIPS: set up the start and end of the array. Set the min_val as first element of the array. 
First check if the array is rotated or not. 
If mid < start. The array is rotated, and right half is ordered. The minimum is between start and mid. The minimum = min(minimum, nums[end]), and Update the end with mid-1. 
If mid > start, check the right half, 
	if end > mid, start, mid, and end are in ordered, return min(min_value, nums[start]). 
	    If end < mid, the right half is rotated, Update min_value and update start with mid + 1.
If end == mid, update min_value = min(min_value, nums[end]), end -=1

The reason why needs to keep the minimum is because the binary search needs assign l = mid + 1, r = mid – 1 (because of mid = (l + r) // 2). Otherwise, the loop can be a dead loop. Need to record the mid-minimum of the mid 

### 540. Single Element in a Sorted Array (Medium)
TIPS: Set a visited set. Loop over the array, if the element is the visited set, delete the key in the set. if not in the element put it into the set. The last element in the set is the single element. This algorithm works only if the element occurrence is two. What about more than two?
If more than two occurrence, first iteration is put the elements into the dictionary, then iteration over the dict, find the key whose value is 1.

### 4. Median of Two Sorted Arrays (Hard)
Binary search:

Another variation: if the array is not sorted, need to two heaps, maximum heap and min heap.

### 875. Koko Eating Bananas
TIPS: binary search from 0 to max of the array. 
```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        left, right = 1, max(piles)

        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if sum([ceil(i / mid) for i in piles]) > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
```

### 34. Find the First and Last Position of the Element in the Sorted Array
TIPS: binary search twice. pay attention to the condition of moving left and right pointer. 
### 274. H-Index
TIPS: binary search of the array, and check the mid value and n-mid, if greater than n-mid, move right, if less than n-mid, move left. return left.
### 2089. Find Target Indices After Sorting Array
TIPS: like 34. Sort the array. Run binary search twice. The first is finding the first element. The second is finding the last element.

### 1060. Missing Element in Sorted Array
Tips: Find the mid-missing number for index idx:
missing = lambda idx: nums[idx] - nums[0] – idx
if k > than missing (last index), return directly. Else the missing value is between num[0] and num[-1]. It is a binary search problem.
### 1062. Longest Repeating Substring
Questions: Is the repeating substring continuous or not?
TIPS: Pay attention if the string allows overlapping string. If allow overlapping string, define a seen set. Window from N-1, iteration from 0, if got a string, check if in the hash table. If not in the hash table, put it into the hash table. If allows overlapping, simply put it in the hash table, if does not allow overlapping index, needs to record the maximum index of the string, when checking if the string is in the hash table need to also check the current string index > maximum index of the hash table. 
Define the length of a repeated substring from N//2 to 1, for every length of substring, iteration over the long string, if seen string in the hash table, return the length. If not seen, put the string on the hash table. Loop the process from N//2 to 1.
```python

class Solution:
    def search(self, L: int, n: int, S: str) -> str:
        """
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        seen = set()
        for start in range(0, n - L + 1):
            tmp = S[start:start + L]
            if tmp in seen:
                return start
            seen.add(tmp)
        return -1

    def longestRepeatingSubstring(self, S: str) -> str:
        n = len(S)

        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if self.search(mid, n, S) != -1:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1
```
The differences are checking whether the hash table is set or dict. Set works for allowing overlapping, while dict works for not allowing overlapping.
Binary search of the string. 
The hash table also works for counting the occurrence.

### 1095. Find in Mountain Array
Option 1: iteration all the elements return true if find the value, if not return False. Time complexity is o(n)
TIPS: In two steps of binary search, find the peak index of the mountain array. Pay attention to the condition of finding the peak. Split the array into two sections and do a binary search separately. Time complexity is o(logN)
```python
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # find the peak
        left = 0
        right = mountain_arr.length() - 1
        peak_ind = 0
        while left < right:
            mid = (left + right) // 2

            mid_val = mountain_arr.get(mid)
            mid_next_val = mountain_arr.get(mid + 1) # the while condition need to be left < right.

            if mid_val < mid_next_val:
                left = mid + 1
            elif mid_val > mid_next_val:
                right = mid
        # peak index is left index
        l_left = 0
        l_right = left

        r_left = left
        r_right = mountain_arr.length() - 1

        min_index = mountain_arr.length()

        while l_left <= l_right:
            mid = (l_left + l_right) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                min_index = min(min_index, mid)
                break
            else:
                if mid_val < target:
                    l_left = mid + 1
                elif mid_val > target:
                    l_right = mid - 1

        while r_left <= r_right:
            mid = (r_left + r_right) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                min_index = min(min_index, mid)
                break
            else:
                if mid_val < target:
                    r_right = mid - 1
                elif mid_val > target:
                    r_left = mid + 1

        if min_index == mountain_arr.length():
            return -1
        else:
            return min_index
```
### 410. Split Array Largest Sum
```python
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def check(arr, guess, k):
            total = 0
            count = 1
            for i in arr:
                if total + i > guess:
                    total = 0
                    count += 1
                total += i
            return count > k

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2
            if check(nums, mid, k): # mid is lower, count > k
                left = mid + 1
            else: # mid is higher or equal, count <= k
                right = mid

        return left
```
### 367. Valid Perfect Square
TIPS: binary search from 0 to n

### 1482. Minimum Number of Days to Make m Bouquets
TIPS: define the ispossible function, and binary search from 0 to maximum element of the array.

### 981. Time Based Key-Value Store
TIPS: binary search the timestamp value
```python
class TimeMap:
    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value , timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.dic.get(key , [])
        l , r = 0 , len(values) - 1
        while l <= r :
            mid = (l + r) >> 1
            if values[mid][1] <= timestamp:
                l = mid + 1
                res = values[mid][0]
            else:
                r = mid - 1
```