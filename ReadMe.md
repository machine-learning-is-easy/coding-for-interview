# String Algorithms - Key Notes

## General Tips
1. **Character Checks:** Iterate through each character; if a condition fails, break and check left/right parts (similar to binary tree search).  
2. **Traversal + Dictionary:** Traverse the string left-to-right or right-to-left, storing information in a dictionary.  
3. **Two Pointers:** Compare two strings, find longest words through deletion, or apply for problems like 809.  
4. **Fixed Window Hash Table:** Convert fixed-length substrings into a hash table for comparison.  
5. **Sliding Window Hash Table:** Convert two-pointer window substrings into a hash table.

---

## Clarifications Before Solving
- Is the problem **case-sensitive**? Lowercase or uppercase?  
- Can input be empty?  
- Can substrings **overlap**?  
- Can characters be **repeated**?

---

## Problem Categories

### A. Group Anagrams
**49. Group Anagrams**  
- Sort each string and use it as a key in a hash table.  
- Collect strings in a list grouped by their sorted key.  

---

### B. Repeating Substrings
**3. Longest Substring Without Repeating Characters**  
- Iterate left-to-right. Track character indices in a hash table.  
- If a duplicate is found, update the anchor: `anchor = max(anchor, hashtable[char])`.  
- Current length = `current_index - anchor`.  

**763. Partition Labels**  
- Keep the last index of each character.  
- The anchor stores the maximum index of all letters in the current segment.

**1668. Maximum Repeating Substring**  
- Multiply the short substring and check if it exists in the long string.  

**1044. Longest Duplicate Substring**  
- Use two pointers `left` and `right` to find duplicates in the remaining string.  

**524. Longest Word in Dictionary through Deleting**  
- Sort dictionary by string length descending.  
- Use two pointers to check if a word can be formed from the string.  

**459. Repeated Substring Pattern**  
- Check substring lengths from `1` to `n//2`.  
- Verify if `substring * (n // substring_length)` equals the string.  

---

### C. Anagram
**438. Find All Anagrams in a String**  
- Fixed-length sliding window.  
- Two hash tables: one for the short string, one for the sliding window.  
- Slide window, update hash table, and compare with target.

---

### D. Permutation
**567. Permutation in String**  
- Similar to anagrams.  
- Check if a substring of the target string is a permutation of the source string.  

---

### E. Partitions
**763. Partition Labels**  
- Track the last index of each character.  
- Create partitions when current index reaches the max last index of visited characters.  

**1763. Longest Nice Substring**  
- Use recursion to split string when a character is not “nice”.  