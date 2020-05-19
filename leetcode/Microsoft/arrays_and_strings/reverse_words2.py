"""
  Reverse Words in a String II
  Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?

"""
from typing import List
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        start=0
        for w in s:
            end=start
            while end < len(s) and s[end]!=" ":
                end+=1
            nextStart = end+1
            while end-1 > start:
                s[start], s[end-1] = s[end-1], s[start]
                start+=1
                end-=1
            start=nextStart
            
    def reverseWords1(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverseList(s, 0, len(s)-1)
        i = 0
        j = 0
        while i < len(s):
            while j < len(s) and s[j] != " ":
                j+=1
            self.reverseList(s, i, j-1)    
            j+=1
            i=j
        
    def reverseList(self, s: List[str], left, right):
        while right > left:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1            

s=Solution()
input=["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
expected=["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
s.reverseWords(input)
print('Output %s:'% input)
print('Expected: %s'% expected)
print('passed: %s'% (input==expected))