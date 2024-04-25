def t(n):
    if 'PM' in n[2]:
        n[2]=n[2].replace('PM', "")
        n=list(map(int,n))
        if(n[0]!=12):
            n[0]=n[0]+12
    elif 'AM' in n[2]:
        
        n[2]=n[2].replace('AM', "")
        n=list(map(int,n))
        if (n[0]==12):
            n[0]=0
    n=f"{n[0]:02d}:{n[1]:02d}:{n[2]:02d}"
    return n


n=list(input().split(':'))
res=t(n)
print(res)
