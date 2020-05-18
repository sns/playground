"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n =   len(matrix)
        if n < 2:
            return
        
        F=0
        L=n-1

        while F<L:
            matrix[F][F], matrix[F][L] = matrix[F][L], matrix[F][F]
            matrix[F][F], matrix[L][L] = matrix[L][L], matrix[F][F]
            matrix[F][F], matrix[L][F] = matrix[L][F], matrix[F][F]
            i=F+1
            while i < L:
                matrix[F][i], matrix[i][L] = matrix[i][L], matrix[F][i]
                matrix[F][i], matrix[L][(L-F)-i] = matrix[L][i], matrix[F][i]
                matrix[F][i], matrix[(L-F)-i][F] = matrix[i][F], matrix[F][i]
                i+=1
            F+=1
            L-=1



s=Solution()
input=[[1,2,3],[4,5,6],[7,8,9]]
expectedOutput=[[7,4,1],[8,5,2],[9,6,3]]
s.rotate(input)
print(input==expectedOutput)