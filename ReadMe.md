# String 
----
## Key Notes:
### 1 Checking all character conditions, if any letter does not satisfy the condition, break the loop, and check the left and right parts of the substring. (Binary tree searching)
### 2 traverse the whole string (from left to right or from right to left) and put it into a dictionary.
### 3 Two pointers to compare two strings. Longest word through deleting. And 809
### 4 convert fixed window substring into a hash table to compare two dictionaries.
### 5 convert two-pointer window substrings into a hash table.
 _____
## Clarify: 
Is it case-sensitive or not? All lower case or upper case?
Input can be empty or not?
can the substring be overlapping or not?
Overlapping selection of character
Repletion of selection of character

## a. Group Anagrams
### 49. Group Anagrams
Tips: sort the string and make the string as the key to the hash table. Put the string into the hash table. Sorting the keys and put the key value from the hash table and put it into a list.

### b.	 Repeating substring
3.longest substring without repeating characters
Iteration from the left to right. Put the current character index to a hash table if no current character in the hash table. If the current character is in the hash table, keep the maximum index encountered during the iteration. Anchor = Max(anchor, hashtable[chr]). The anchor will be the maximum index of the duplicate character in the visited string. Then assign the current character index to the value of the hash table. The length of the non-repeating string is the current index – anchor. The anchor should be staring at -1 (some of the iterations begin -1)
Compare with 763. Partition Labels. 
763 needs to keep the index of last seen in the entire string, 3, the anchor only needs to keep the maximum index of all letters.

### 1668. Maximum Repeating Substring
TIPS: This is checking the maximum occurrence of the short substring in the long string. Try to multiply the substring, and check if the multiplied substring is in the long string or not. If yes, continue to multiply the substring.

### 1044. Longest Duplicate Substring (Hard)
TIPS: initiate left and right index as 0, checking if the current index in the rest half of the string [right_index:], if yes, increase right_index, and keep the longest index. If no, increase both the left and right index.

### 524. Longest Word in Dictionary through Deleting (two pointer)
TIPS: sort the dictionary by the length of the string in descending order. Iteration on a sorted array, on each element, check the if every word letter in the long string. If yes, move both check the next letter, if not, keep the word letter the same, move the next letter of the long string. 

###  459. Repeated Substring Pattern
TIPS: starting from 1 to n//2 + 1. Find if the whole string can be formed by multiply substring * n//n_substring

## c.	Anagram
### 438. Find All Anagrams in a String
Tips: fix the length sliding window (the window size is fixed on the length of the shorter string).  Two hash table. The first hash table is the shorter string. The second hash table keeps the sliding window string in the long string. Put the short string into a hash table. Start iteration over the entire string. If start < length, add character to the hash table (begin to add to hash table), else add current character to hash table, delete current index – length from the hash table. If current hash table == searched anagram hash table, then return True. The second hash table updates with the start and the end of sliding windows. end of sliding widow add key or add key value of the hash table. The start of hash table deletes key or decrease key value in hash table.

## d.	permutation
### 567. Permutation in String
TIPS: This is the same as the anagram of a long string. The window length is given in the substring.
Case sensitive?
Return How many times or yes or no?
Allow overlapping?

## e.	Partitions
### 763. Partition Labels
Tips: each letter appears in one partition. Create a hash table, the key is a character, value of the key is the last index seen in the string while looping over the string from left to right. Iteration over the string from left, keep the start of the segment. Keep all the visited character's maximum last index at variable J. If see a letter index equal J. save the current substring to the result. Length of substring.

### 1763. Longest Nice Substring (a pattern)
The longest, nice substring needs to be consecutive. So, if one character is not a nice substring. We can split the string into left and right until all the string is the nice substring.
````
class Solution:
    @lru_cache()
    def longestNiceSubstring(self, s: str) -> str:
        # Edge case
        if len(s) < 2:
            return ""

        nice = ""  # Store the longest nice substring
        for i in range(len(s)):
            # checking every character, upper case and lower case, if find one letter upper case or lower case is not
            # in the string, will split the string and recursive call left half and right half, find the maximum length
            # and return the maximum length
            if s[i].lower() in s and s[i].upper() in s:
                nice += s[i]
            else:
                leftPart = self.longestNiceSubstring(s[:i])
                rightPart = self.longestNiceSubstring(s[i + 1:])
                return leftPart if len(leftPart) >= len(rightPart) else rightPart
        return nice
````

checking each letter in lower case and upper case. If all apply, return the string, if not split the string and check left and right patrician of the string

### 1048. Longest String Chain
TIPS: sort all the words by length in descending order. Define a DICT of each word, the value is the word level. Level means the index of the string chain. Each word is in the string chain. Iteration from the word list. try to delete each character of the word and form a new word, if a new word is in the dictionary and the dict[current_word] < dict[new_word] + 1, assign the dict[current_word]= dict[new_word] + 1. The maximum value of the dictionary is the maximum length of the chain.

## f.	longest palindromic substring
TIPS: a palindromic can be an odd or even string. Define a function IsPalindromic starting from the index, left and right. Return all palindromic from the current index. In the main function check if IsPalindromic(current_index, current_index) and IsPalindromic(current_index, current_index +1)

### 516. Longest Palindromic Subsequence
TIPS: can ignore some elements without changing the order of the remaining elements.

````
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def dfs(i, j):
            if i < 0 or j >= len(s):
                return 0
            elif s[i] == s[j]:
                if i == j:
                    return 1 + dfs(i - 1, j + 1)
                else:
                    return 2 + dfs(i - 1, j + 1)
            else:
                return max(dfs(i - 1, j), dfs(i, j + 1))
        max_len = 0
        for ind in range(len(s)):
            max_len = max(max_len, dfs(ind, ind), dfs(ind, ind + 1))
        return max_len
````


## g.	Regular Expression Matching
TIPS: matching current letter matching. If the first two letters is “{}*”. {} is a letter. There are two situations, the first is * is 0. Return the current string and skip the two letters in the pattern.  The second is * >= 1. Return the matchfirstletter and skip the first letter and match the next letter and current pattern. If the pattern does not include “{}*”, return matchfirstletter and skit the first letter and skip the first pattern.  
### 10. Regular Expression Matching

````
class Solution(object):
    @lru_cache()
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
````

## h.	Fast and slow pointer
https://leetcode.com/problems/linked-list-cycle-ii/

## i.	Moving sliding window
### 76. Minimum Window Substring:  
TIPS: We have long string t and short string s. short string s includes all the letters we are searching for. We can count all letters in s and create a s_dict which includes all letters in s as in keys, and the value of the keys are times the letter appears in s. The dictionary is the requirements for which letter of the substring of t needs to have and how many of those letters need to have. Then we can define two points, the start and end points. At the beginning, start and end point to the very beginning of the long string s. First, we fix the start and move the end to the right. Meanwhile, we keep a dictionary of substrings between the start and end, when the end moves right, we increase the corresponding letter value by 1. Also, we check if the dictionary between start and end meets the requirements or not.  We keep moving the end to the right until meet all the requirements. Next, we fix the end pointer and move the start pointer to the right. When move the start pointer to the right, we decrease the value of the keys, until the requirements are met.  In the process, we keep a record of the minimum substring length which meets the requirement. Repeat the process until the end reaches the end of the long string.

### 680. Valid Palindrome II (Easy)
Tips: two pointer variations, left and right pointer moves from every character, left move left, right move right and compare the left and right character, if they match, continue to move. Otherwise, break the loop. Be careful. There are two types of palindrome string. Even palindrome and odd palindrome. For even palindromes, left, and right start from 0, and 1. For odd palindrome strings, left, and right start from 0, 0

### 524. Longest Word in Dictionary through Deleting (Medium) (pattern matching)
Tips: sort the dictionary from longest to shortest, matching if each word in the s (two pointers from starting to the end)

### 267. Palindrome Permutation II
TIPS: panlindrom + DFS. 1. Convert the original text into dictionary by counter. Add the odd number of at beginning. To make sure the rest of the letter is even. Then dfs the dictionary key, in one loop add left and right of the same key. Until the result length == length of the original string.

### 336. Palindrome Pairs
TIPS:  Put the string in reverse hashmap. The key is the reverse string, and the value is the index. Check conditions of palindrome Paris. Iteration over the string, consider the backward string on left and backward string on right, backward string == normal string.

### 340. Longest Substring with At Most K Distinct Characters (Hard)
Similar with 76. The difference is 76 need to record the target s dictionary while 340 only need to count the distinct letter.
Two points pointing to the beginning of the string. Keep a record of distinct characters with a hash table. The value of the keys is the number of occurrences. If the hash table has more than K values, move the left pointer. If the hash table has K keys(), move the right pointer.

````
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0
        hashtable = collections.defaultdict(int)

        ans = 0
        prev = 0
        for ind, l in enumerate(s):
            hashtable[l] += 1
            while prev < len(s) and len(hashtable) > k:
                hashtable[s[prev]] -= 1
                if hashtable[s[prev]] <= 0:
                    del hashtable[s[prev]]
                prev += 1

            ans = max(ans, ind - prev + 1)
        return ans
````

### 809. Expressive Words
Two pointers to two strings, count the same character, check the numbers, and move to the next compare. Pay attention to find the next same element index and compare n with n+1.

````
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def similary(long_s, short_s):
            n = len(long_s)
            m = len(short_s)

            idx_n, idx_m = 0, 0

            while idx_n < n and idx_m < m:
                if long_s[idx_n] != short_s[idx_m]:
                    return False

                c_n = long_s[idx_n]
                num_c_n = 1
                while idx_n + 1 < n and long_s[idx_n + 1] == c_n:
                    idx_n += 1
                    num_c_n += 1

                num_c_m = 1
                while idx_m + 1 < m and short_s[idx_m + 1] == c_n:
                    idx_m += 1
                    num_c_m += 1

                if num_c_n == num_c_m or (num_c_n >= num_c_m and num_c_n >= 3):
                    idx_m += 1
                    idx_n += 1
                else:
                    return False

            if idx_n == n and idx_m == m:
                return True
            return False

        total_n = 0
        for word in words:
            if similary(s, word):
                total_n += 1

        return total_n
````

### 424. Longest Repeating Character Replacement
Window function. Keep front and back pointer.
TIPS, this type of question format is recursively called a function which can match one letter or one word. The parameter in the next recursive call will be shorter. Until all the letters matched
TIPS: keep the dictionary in windows. If front – back + 1 – max(count.values()) > k, move left. Else: record the maximum length.
````
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        back = 0
        max_len = 0
        for front, char in enumerate(s):
            count[char] += 1
            if front - back + 1 - max(count.values()) > k:
                count[s[back]] -= 1
                back += 1
            else:
                max_len = max(max_len, front - back + 1)

        return max_len
````

### 1358. Number of Substrings Containing All Three Characters
TIPS: moving window and keep the dictionary. For each interval, all possible strings are n-right (all possible string on the right)

### 159. Longest Substring with At Most Two Distinct Characters

````
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        count, i = {}, 0
        max_len = 0
        for j, k in enumerate(s):
            count[k] = count.get(k, 0) + 1
            if len(count) > 2:
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    del count[s[i]]
                i += 1

            if len(count) <= 2:
                max_len = max(max_len, j - i + 1)
        return max_len
````

### 2024. Maximize the Confusion of an Exam
TIPS: the same with 424. Longest Repeating Character Replacement keeps the keys and value of the sliding windows,  

### 209. Minimum Size Subarray Sum
TIPS: iteration over the array from left to right, keep the accumulative sum of the element, keep the sum of the subarray as the key in a dictionary, the value is the index of current element, check if the accumulative_sum – targe in the dictionary, if yes, the length is current index – dictionary[accumulative_sum], keep the minimum of the length.

j.	Hash table to count string.
### 1002. Find Common Characters
TIPS: find the first word dictionary word0_dict by the counter. Iteration over the next words, convert the next words to dictionary word_dict. Loop over all the keys in first words dictionary. If the key not in the word_dict, del the key, if in the word0_dict. Assign the value of word0_dict to the min(word0_dict[key], word_dict[key])

k.	String matching
### 79. Word Search
TIPS: 2D string matching, set the visited hash table, backtracking each element in the 2D array. 

l.	Two pointers
### 1055. Shortest Way to Form String
TIPS: two pointers to the source and target. If matched, move two pointers next. If not matched move the source pointer only. If the source point reaches the end, the source point is assigned to be 0 (search the source again). And the minimum required + 1.

### 941. Valid Mountain Array
TIPS: from the start iteration, if the next element is greater than the current element, increase the start until the next element is lower than the current element. Iteration from the end of the array, if the previous element is higher than the current element, move end to the left. If start == end and start >0 and end < len(arr) – 1. Because need to guarantee start and end should at least move one element.
````
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        start, end, L = 0, len(arr) - 1, len(arr)

        while start < L-1 and arr[start] < arr[start+1]:
            start += 1
        while end > 0 and arr[end] < arr[end-1]:
            end -= 1
        # need at lease one element for start and at least one element for end
        return start == end and 0 < start and end < len(arr) - 1
````


m.	Common prefix
### 14. Longest Common Prefix

n.	String Distance
### 161. One Edit Distance
Tips: get the index of which two string letter does not match. Then check the rest of the left string.

o.	String to number
### 171. Excel Sheet Column Number
TIPS: iteration from left to right. ans = ans * 16 + digit_of_the_letter.

### 168. Excel Sheet Column Title
TIPS: convert the number to excel sheet column number. Need divmod(columnNumber – 1, 26)
````
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber:
            # there is no A0 in the expression, need to minus 1, to gurantee there is some value
            # in the lowest priority digit
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            ans = chr(65 + remainder) + ans
        return ans
````

### 383. Ransom Note
TIPS: Counter the magazine string. keep the number of each character. Iteration the ransomNote from left to right. check if the character of ransomNote in the dictionary, if yes, decrease by 1, if ==0 after decrease, remove the key. If not in the dictionary, return False.

### 316. Remove Duplicate Letters

````
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occ = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                # this is checking the last element of the stack. if last element of the stack
                # has duplicates, and current letter < last element, should remove the letter.
                while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)

        return ''.join(stack)
````

### 1980. Find Unique Binary String
TIPS: iteration over the numbers, compare index
````
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""

        index = 0
        for bin_num in nums:
            # if change one digit, the result will different from current number,
            # iteration from all numbers, it mean the ans will different from all number
            ans = ans + str(1 - int(bin_num[index]))
            index += 1
        return ans
````