na=int(input())
la=[input() for _ in range(na)]
qa=int(input())
lq=[input() for _ in range(qa)]
lc=[]
for i in lq:
    count=0
    for j in la:
        if i==j:
            count+=1
    lc.append(count)
    
        
for i in lc: print(i)
