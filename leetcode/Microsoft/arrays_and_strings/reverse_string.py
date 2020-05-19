"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List
class Solution:
    def reverseString(self, s:List[str]) -> None:
        i, j = 0, len(s)-1
        while j > i:
            s[i], s[j] = s[j], s[i] 
            i+=1
            j-=1
s=Solution()
input=["h","e","l","l","o"]
expected=["o","l","l","e","h"]
s.reverseString(input)
print('Output: %s'% input)
print('Expected: %s'%expected)
print('Passed: %s'% (input==expected))