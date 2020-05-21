"""
1246. Palindrome Removal

Given an integer array arr, in one move you can select a palindromic subarray arr[i], arr[i+1], ..., arr[j] where i <= j,
and remove that subarray from the given array. Note that after removing a subarray,
the elements on the left and on the right of that subarray move to fill the gap left by the removal.

Return the minimum number of moves needed to remove all numbers from the array.

Example 1:

Input: arr = [1,2]
Output: 2

Example 2:

Input: arr = [1,3,4,1,5]
Output: 3
Explanation: Remove [4] then remove [1,3,1] then remove [5].
 
Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 20
"""
from typing import List
import functools
class Solution:
    def minimumMoves0(self, arr: List[int]) -> int:
        # dp[i][j] = minumum number of moves to delete elements from i to j
        dp=[[float("inf")] * len(arr) for i in range(len(arr))]
        
        for i in range(len(arr)-1, -1, -1):
            for j in range(i, len(arr)):
                if i==j:
                    dp[i][j]=1
                elif j-i==1:
                    dp[i][j] = 1 if arr[i]==arr[j] else 2
                else:
                    m=float("inf")
                    for k in range(i, j):
                        m = min(m, dp[i][k] + dp[k+1][j])
                    
                    if(arr[i] == arr[j]):
                        dp[i][j]=min(m, dp[i+1][j-1])
                    else:
                        dp[i][j]=m
        return dp[0][len(arr)-1]

    def minimumMoves(self, arr: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(i: int , j: int) -> int:
            if j < i:
                return 0
            if i == j:
                return 1
            if j-i==1:
                return 1 if arr[i]==arr[j] else 2
            
            minMoves = len(arr)
            for k in range(i, j):
                minMoves = min(minMoves, dp(i, k) + dp(k+1,j))
            if(arr[i]==arr[j]):
                return min(minMoves, dp(i+1, j-1))
            return minMoves
        return dp(0, len(arr)-1)
            
s=Solution()
input=[1,2]
expected=2
output= s.minimumMoves(input)
print('input %s:'% input)
print('Output %s:'% output)
print('Expected: %s'% expected)
print('passed: %s'% (output==expected))
input=[1,3,4,1,5]
expected=3
output= s.minimumMoves(input)
print('input %s:'% input)
print('Output %s:'% output)
print('Expected: %s'% expected)
print('passed: %s'% (output==expected))