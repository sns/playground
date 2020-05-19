"""
  Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

"""

class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        mapping={")": "(", "}": "{", "]": "["}
        for p in s:
            if(len(stack) > 0):
                top = stack[-1]
                if p in mapping:
                    if top != mapping[p]:
                        return False
                    stack.pop()
                else:
                    stack.append(p)
            else:
                stack.append(p)
        return len(stack)==0
s=Solution()
input="{[]}"
expected=True
output= s.isValid(input)
print('Output %s:'% output)
print('Expected: %s'% expected)
print('passed: %s'% (output==expected))
input="(]"
expected=False
output= s.isValid(input)
print('Output %s:'% output)
print('Expected: %s'% expected)
print('passed: %s'% (output==expected))
input="([)]"
expected=False
output= s.isValid(input)
print('Output %s:'% output)
print('Expected: %s'% expected)
print('passed: %s'% (output==expected))