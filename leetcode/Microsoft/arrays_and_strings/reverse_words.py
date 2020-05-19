"""
Reverse Words in a String

Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s.strip().split())
        l.reverse()
        return " ".join(l)

s=Solution()
input="the sky is blue"
expected= "blue is sky the"
output= s.reverseWords(input)
print('Output :%s'% output)
print('Expected: %s'% expected)
print('passed: %s'%(output==expected))
input="  hello world!  "
expected= "world! hello"
output= s.reverseWords(input)
print('Output %s:'% output)
print('Expected: %s'% expected)
print('passed: %s'% (output==expected))
input="a good   example"
expected="example good a"
output= s.reverseWords(input)
print('Output %s:'% output)
print('Expected: %s'% expected)
print('passed: %s'% (output==expected))