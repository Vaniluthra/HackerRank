n, q = map(int, input().split())
arr = [[] for _ in range(n)]
lastAns = 0

for _ in range(q):
    inp = list(map(int, input().split()))
    query_type = inp[0]

    if query_type == 1:
        index = (inp[1] ^ lastAns) % n
        arr[index].append(inp[2])
    elif query_type == 2:
        index = (inp[1] ^ lastAns) % n
        index_before = inp[2] % len(arr[index])
        lastAns = arr[index][index_before]
        print(lastAns)
