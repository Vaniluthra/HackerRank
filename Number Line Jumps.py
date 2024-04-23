def will_meet(x1, v1, x2, v2):
    if (x1 > x2 and v1 > v2) or (x1 < x2 and v1 < v2):
        print('NO')
        return
    
    if v1 == v2:
        if x1 == x2:
            print('YES')
        else:
            print('NO')
        return
    
    meeting_point = (x2 - x1) % (v1 - v2)
    if meeting_point == 0:
        print('YES')
    else:
        print('NO')

x1, v1, x2, v2 = map(int, input().split())

will_meet(x1, v1, x2, v2)
