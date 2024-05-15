def round(n):
    a=(n//5)+1
    diff=(a*5)-n
    if diff<3:
        return a*5
    else :
        return n
n=int(input())
a=[int(input()) for _ in range(n)]
for i in a:
    if i>=38:
        res=round(i)
        print(res)
    else:
        print(i)

