"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix is None or len(matrix)==0:
            return []
        R=len(matrix)
        C=len(matrix[0])

        seen=[[False]*C for _ in range(R)]
        dr=[0, 1, 0, -1]
        dc=[1, 0, -1, 0]
        c, r, di = 0, 0, 0
        res = []
        for _ in range(R*C):
            res.append(matrix[r][c])
            seen[r][c]=True
            
            cr = r+dr[di]
            cc = c+dc[di]

            if 0 <= cr <R and 0 <= cc < C and not seen[cr][cc]:
                r=cr
                c=cc
            else:
                di=(di+1)%4
                r=r+dr[di]
                c=c+dc[di]
        
        return res

    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        if matrix is None or len(matrix) == 0:
            return []
        m = len(matrix)
        if m == 1:
            return matrix[0]
        n = len(matrix[0])
        res = []
        cs=0
        ce=n-1
        rs=0
        re=m-1
        while cs < ce and rs < re:
            for i in range(cs, ce):
                res.append(matrix[rs][i])
            for i in range(rs, re):
                res.append(matrix[i][ce])
            for i in range(ce, cs, -1):
                res.append(matrix[re][i])
            for i in range(re, rs, -1):
                res.append(matrix[i][cs])
            cs+=1
            ce-=1
            rs+=1
            re-=1

        if rs==re and cs==ce:
            res.append(matrix[rs][cs])
        
        elif rs==re:
            for i in range(cs, ce+1):
                res.append(matrix[rs][i])
        elif cs==ce:
            for i in range(rs, re+1):
                res.append(matrix[i][cs])

        return res


s = Solution()
input=[[1,2,3],[4,5,6],[7,8,9]]
output=[1,2,3,6,9,8,7,4,5]
print(output==s.spiralOrder(input))