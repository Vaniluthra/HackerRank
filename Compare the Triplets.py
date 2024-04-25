def scoreCalc(a,b):
    pointA,pointB=0,0

    for i in range(3):
        if(a[i]>b[i]):
            pointA+=1
        elif(b[i]>a[i]):
            pointB+=1
    res=[pointA,pointB]
    return res

a=list(map(int,input().split()[:3]))

b=list(map(int,input().split()[:3]))


res=scoreCalc(a,b)

print(res[0],res[1])
    
    
