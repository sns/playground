"""
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None or len(height) == 0:
            return 0
        totalWater = 0
        length = len(height)
        leftMax = [0]*length
        rightMax = [0]*length
        leftMax[0] = height[0]
    
        for i in range(length):
            leftMax[i] = max(height[i], leftMax[i -  1])
        
        rightMax[length - 1] = height[length - 1]
    
        for i in range(length-2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i + 1])
    
        for i in range(length):
            totalWater += min(leftMax[i], rightMax[i]) - height[i]
    
        return totalWater

s = Solution()
print(s.trap([1,0,2]))