"""
Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        n=len(s)
        startEndLength=(0,0,1)
        def expandAround(s: str, left:int, right: int):
            i=left
            j=right
            while 0<=i and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            i+=1
            j-=1
            return [i, j, j-i+1]
        for i in range(n):
            p1 = expandAround(s, i, i)
            p2 = expandAround(s, i, i+1)
            if p1[2] > p2[2] and p1[2] > startEndLength[2]:
                startEndLength=p1
            elif p1[2] < p2[2] and p2[2] > startEndLength[2]:
                startEndLength=p2

        return s[startEndLength[0]: startEndLength[1]+1]

    def longestPalindrome1(self, s: str) -> str:
        
        n = len(s)
        if n==0 or n==1:
            return s
        
        startEndLength = [0, 0, 1]
        for i in range(n):  
            self.longest_palindrome_for_single_point(s, n, startEndLength, i, i)
            self.longest_palindrome_for_single_point(s, n, startEndLength, i, i+1)
            
        return s[startEndLength[0]: (startEndLength[1]+1)]
      
    def longest_palindrome_for_single_point(self, s: str, n: int, startEndLength: list, left: int, right: int):
        
        while left>=0 and right<n and s[left]==s[right]:
            left -= 1
            right += 1
        
        left += 1
        right -= 1
        length = right-left+1
        
        if startEndLength[2]<length:
            startEndLength[0] = left
            startEndLength[1]= right
            startEndLength[2]=length

        return
   
    def longestPalindrome2(self, s: str) -> str:     
        n = len(s)
        if n==0 or n==1:
            return s
        
        isPld = [[False]*n for _ in range(n)]
        
        start, end, maxLength = 0, 0, 1        
        length = 2     
        while length<=n:      
            left = n-length 
            
            while left>=0:
                right = left+length-1                
                if length<=3:
                    isPld[left][right] = (s[left]==s[right])
                else:
                    isPld[left][right] = (isPld[left+1][right-1] and s[left]==s[right]) 
                    
                if isPld[left][right] and maxLength!=length:
                    start, end, maxLength = left, right, length
                    
                left -= 1
                
            if maxLength-length==2:
                break
            else:
                length += 1
            
        return s[start: (end+1)]        
    
    def longestPalindrome3(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        
        chars = []
        count = 0
        i = 0
        j = len(s) - 1
        
        while j > i:
            if s[i] == s[j]:
                count += 2
                chars.append(s[i])
            i+=1
            j-=1
        scount = count
        if i==j:
            chars.append(s[i])
            count +=1
            if s[i] == s[i-1] and s[i] != s[i+1]:
                k = i-1
                while  k >= 0 and s[k] == s[i]:
                    chars.append(s[k])
                    count +=1
                    k -=1
            if s[i] == s[i+1] and s[i] != s[i-1]:
                k = i+1
                while k < len(s) and s[k] == s[i]:
                    chars.append(s[k])
                    count +=1
                    k += 1

        for k in range(scount//2):
            chars.append(chars[k]) 
            
        return "".join(chars) if count > 0 else s[i]

    memo={}
    def longestPalindrome4(self, s: str) -> str:
        if len(s) < 2:
            return s
        self.memo = {}
        ans=(0,0)
        for i in range(0, len(s)-1):
            for j in range(i, len(s)):
                    ans = (i, j) if self.isPalindrome(s, i, j) and j-i > ans[1]-ans[0] else ans
        return s[ans[0]: ans[1]+1]
    
    def isPalindrome(self, s: str, i: int, j: int):
        if (i, j) not in self.memo:
            if i==j:
                self.memo[(i, j)]=True
            elif i==j-1:
                self.memo[(i, j)] = s[i] == s[j]
            else:
                self.memo[(i, j)] = self.isPalindrome(s, i+1, j-1) and s[i] == s[j]
        return self.memo[(i, j)]

s=Solution()
input="babad"
expected="bab"
output= s.longestPalindrome(input)
print('Output %s:'% output)
print('Expected: %s'% expected)
print('passed: %s'% (output==expected))
input="abacab"
expected="bacab"
output= s.longestPalindrome(input)
print('Output %s:'% output)
print('Expected: %s'% expected)
print('passed: %s'% (output==expected))
input="cbbd"
expected="bb"
output= s.longestPalindrome2(input)
print('Output %s:'% output)
print('Expected: %s'% expected)
print('passed: %s'% (output==expected))
input="vmqjjfnxtyciixhceqyvibhdmivndvxyzzamcrtpywczjmvlodtqbpjayfchpisbiycczpgjdzezzprfyfwiujqbcubohvvyakxfmsyqkysbigwcslofikvurcbjxrccasvyflhwkzlrqowyijfxacvirmyuhtobbpadxvngydlyzudvnyrgnipnpztdyqledweguchivlwfctafeavejkqyxvfqsigjwodxoqeabnhfhuwzgqarehgmhgisqetrhuszoklbywqrtauvsinumhnrmfkbxffkijrbeefjmipocoeddjuemvqqjpzktxecolwzgpdseshzztnvljbntrbkealeemgkapikyleontpwmoltfwfnrtnxcwmvshepsahffekaemmeklzrpmjxjpwqhihkgvnqhysptomfeqsikvnyhnujcgokfddwsqjmqgsqwsggwhxyinfspgukkfowoxaxosmmogxephzhhy"
expected="oxaxo"
output= s.longestPalindrome2(input)
print('Output %s:'% output)
print('Expected: %s'% expected)
print('passed: %s'% (output==expected))