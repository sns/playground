"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for s in strs:
            counter=[0]*26
            for c in s:
                counter[ord(c)-ord('a')]+=1
            key = tuple(counter)
            if key not in ans:
                ans[key] = [s]
            else:
                ans[key].append(s)
        
        return list(ans.values())

s=Solution()
input=["eat","tea","tan","ate","nat","bat"]
expected=[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
output=list(map(lambda x: sorted(x), s.groupAnagrams(input)))
print("%s\nOutput: %s\nExpected: %s"%(output==expected, output, expected))