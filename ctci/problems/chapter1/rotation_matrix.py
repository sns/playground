# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# Write a method to rotate the image by 90 degrees. Can you do this in place?

# 1 2      3 1
# 3 4      4 2
# 
# 1 2 3    7 4 1
# 4 5 6    8 5 2 
# 7 8 9    9 6 3
# 
# 01 02 03 04   13 09 05 01
# 05 06 07 08   14 10 06 02
# 09 10 11 12   15 11 07 03
# 13 14 15 16   16 12 08 04
# #
def rotate(m: [[int]], N):
    print("The Original matrix")
    print(m)

    res: [[int]] = []
    
    F = 0
    L = N - 1

    while L > F:
        m[F][F], m[F][L] = m[F][L], m[F][F]
        m[F][F], m[L][L] = m[L][L], m[F][F]
        m[F][F], m[L][F] = m[L][F], m[F][F]

        i = F + 1
        while i < L:
            m[F][i], m[i][L] = m[i][L], m[F][i]
            m[F][i], m[L][L-i] = m[L][L-i], m[F][i]
            m[F][i], m[L-i][F] = m[L-i][F], m[F][i]
            i += 1
        F += 1
        L -= 1
    
    print("The Rotated Matrix:")
    print(m)

    return m

def creatMatrix(size: int):
    m:[[int]] = []

    for i in range(size):
        n = []
        for j in range(size):
            n.append((i * size) + j + 1)
        m.append(n)
    return m

def solve():
    s = 2
    m = creatMatrix(s)
    rotate(m , s)
    s = 3
    m = creatMatrix(s)
    rotate(m , s)
    s = 4
    m = creatMatrix(s)
    rotate(m , s)