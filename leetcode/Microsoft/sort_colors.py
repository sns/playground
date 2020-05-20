"""
Sort Colors:
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # curent index 
        curr=0
        n = len(nums)
        #the index after the last 0
        p0=0
        #the index before the first 2
        p2=n-1
        
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1      
s=Solution()
input=[2,0,2,1,1,0]
print('input %s:'% input)
expected=[0,0,1,1,2,2]
s.sortColors(input)
print('Output %s:'% input)
print('Expected: %s'% expected)
print('passed: %s'% (input==expected))
input=[1,2,0]
print('input %s:'% input)
expected=[0,1,2]
s.sortColors(input)
print('Output %s:'% input)
print('Expected: %s'% expected)
print('passed: %s'% (input==expected))
input=[2,0,1]
print('input %s:'% input)
expected=[0,1,2]
s.sortColors(input)
print('Output %s:'% input)
print('Expected: %s'% expected)
print('passed: %s'% (input==expected))
input=[2,1,2]
print('input %s:'% input)
expected=[1,2,2]
s.sortColors(input)
print('Output %s:'% input)
print('Expected: %s'% expected)
print('passed: %s'% (input==expected))
