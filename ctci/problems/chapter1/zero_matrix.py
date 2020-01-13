# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
    
def zero_matrix(matrix, m,  n):
    print("The original matrix: ")
    print(matrix)
    rows = set()
    cols = set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if (i in rows) == False:
                    rows.add(i)
                if (j in cols) == False:
                    cols.add(j)
    
    for i in rows:
        for j in range(n):
            matrix[i][j] = 0
    
    for j in cols:
        for i in range(m):
            matrix[i][j] = 0
    print("The result matrix:")
    print(matrix)

def solve():
    #m=[[1,2,0], [2,0,3], [1,2,3], [5,6,7]]
    m = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    zero_matrix(m, 5, 4)