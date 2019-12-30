# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

# Example 1:

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
 
# Note:

# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].

class Solution:
    
    def findPermutations(self, input: str, prefix: str, res: set) -> set:
        if len(input) == 0:
            if (prefix in res) == False:
                res.add(prefix)
        for (i, char) in enumerate(input):
            remaining = input[0:i] + input[i+1:]
            self.findPermutations(remaining, prefix + char, res)
        return res
    
    def findSubstringsBySize(self, input: str, size: int):
        substrings = set()
        for (k, v) in enumerate(input):
            if k + size <= len(input):
                substring = input[k: size + k]
                if ( substring in substrings) == False:
                    substrings.add(substring)
        return substrings
          
    def checkInclusionNotEfficient(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        permutationsSet = set()
        permutations = self.findPermutations(s1, "", permutationsSet)
        substrings = self.findSubstringsBySize(s2, len(s1))
        
        for p in permutationsSet:
            if p in substrings:
                return True
        return False
    
    def match(self, s1_map, s2_map):
        for i in range(26):
            if s1_map[i] != s2_map[i]:
                return False
        return True
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = []
        s2_map = []
        for i in range(26):
            s1_map.append(0) 
            s2_map.append(0)
        for (i, char) in enumerate(s1):
            s1_map[ord(char) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] += 1
        for i in range(len(s2) - len(s1)):
            if self.match(s1_map, s2_map):
                return True
            s2_map[ord(s2[len(s1) + i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] -= 1

        return self.match(s1_map, s2_map)

    def checkInclusionRewrite(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False
        s1_map = []
        s2_map = []
        for i in range(26):
            s1_map.append(0)
            s2_map.append(0)
        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] += 1
        
        for i in range(len(s2) - len(s1)):
            if self.map_arrays_equals(s1_map, s2_map):
                return True
            s2_map[ord(s2[len(s1) + i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] -=1
        
        return self.map_arrays_equals(s1_map, s2_map)
    
    def map_arrays_equals(self, s1_map, s2_map):
        for i in range(26):
            if s1_map[i] != s2_map[i]:
                return False
        return True

def solve():
    solution = Solution()
    string1 = "ab"
    string2 = "eidbaooo"
    print(solution.checkInclusionNotEfficient(string1, string2))
    print(solution.checkInclusionRewrite(string1, string2))