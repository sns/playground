"""
Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0 and len(nums1) > 0:
            nums1[:] = nums2[:] 
            return
        if n==0:
            return
        i=m-1
        j=n-1
        k=m+n-1
        while k >= 0:
            if i>=0 and j>=0:
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i-=1
                    k-=1
                else:
                    nums1[k] = nums2[j]
                    j-=1
                    k-=1
            elif i>=0:
                nums1[k] = nums1[i]
                i-=1
                k-=1
            else:
                nums1[k] = nums2[j]
                j-=1
                k-=1
            
s=Solution()
nums1=[1,2,3,0,0,0]
print('nums1 %s:'% nums1)
m=3
nums2=[2,5,6]
print('nums2 %s:'% nums2)
n=3
expected=[1,2,2,3,5,6]
s.merge(nums1, m, nums2, n)
print('Output %s:'% nums1)
print('Expected: %s'% expected)
print('passed: %s'% (nums1==expected))