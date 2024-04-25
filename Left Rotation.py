n,d=map(int,input().split())
a=list(map(int,input().split()))
an=[0]*n
for i in range(n):
    an[i-d]=a[i]
    
print (' '.join(map(str,an)))
