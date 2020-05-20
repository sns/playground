"""
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        inputUniqueWordSets = [set(s) for s in arr if len(s)==len(set(s))]
        uniqueSets=[set()]
        maxLength=0

        for wordSet in inputUniqueWordSets:
            for prevUniqueSet in uniqueSets[:]:
                combo = wordSet | prevUniqueSet
                if len(combo) == len(wordSet) + len(prevUniqueSet):
                    uniqueSets.append(combo)
                    maxLength=max(maxLength, len(combo))
        return maxLength

s=Solution()
input=["un","iq","ue"]
expected=4
output= s.maxLength(input)
print('input %s:'% input)
print('Output %s:'% output)
print('Expected: %s'% expected)
print('passed: %s'% (output==expected))