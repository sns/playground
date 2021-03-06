"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while j >= i:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        
        return True

s=Solution()
input="A man, a plan, a canal: Panama"
expected=True
print("Output: %s\nExpected: %s"% (s.isPalindrome(input), expected))