def f(s,t,a,b,mc,nc):
    ap,o=0,0
    for i in range(len(mc)):
        mc[i]=mc[i]+a
        if mc[i]>=s and mc[i]<=t:
            ap+=1
    for i in range(len(nc)):
        nc[i]=nc[i]+b
        if nc[i]>=s and nc[i]<=t:
            o+=1

    print(ap,o,sep='\n')
s,t = map(int, input().split())
a,b = map(int, input().split())
m,n = map(int, input().split())
mc= list(map(int, input().split()))
nc= list(map(int, input().split()))
f(s,t,a,b,mc,nc)
