def diagonalDifference(mat):
    row=len(mat)
    
    sumLeftToRight,sumRightToLeft=0,0
    for i in range(row):
        sumLeftToRight+=mat[i][i]
        sumRightToLeft+=mat[i][row-1-i]

    
    
    return abs(sumLeftToRight-sumRightToLeft)

rows=int(input())

mat = []
for _ in range(rows):
    row=list(map(int,input().split()))
    mat.append(row)

diff=diagonalDifference(mat)
print(diff)
