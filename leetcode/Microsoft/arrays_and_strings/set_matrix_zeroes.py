"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
----------------------------------------------
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
----------------------------------------------
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
-----------------------------------------------
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # memo = ({}, {})
        # m = len(matrix)
        # n = len(matrix[0])

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             if i not in memo[0]:
        #                 memo[0][i] = True
        #             if j not in memo[1]:
        #                 memo[1][j] = True                        
        # for i in memo[0]:
        #     matrix[i][:n]=[0]*n
        # for i in range(m):
        #     for j in memo[1]:
        #         matrix[i][j] = 0

        rows = set()
        cols = set()
        m = len(matrix)
        n = 0 if len(matrix) == 0 else len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if (i not in rows):
                        rows.add(i)
                    if (j not in cols):
                        cols.add(j)

        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

        for j in cols:
            for i in range(m):
                matrix[i][j] = 0


s = Solution()
input = [[1,1,1],[1,0,1],[1,1,1]]
output = [[1,0,1],[0,0,0],[1,0,1]]
s.setZeroes(input)
print(input == output)